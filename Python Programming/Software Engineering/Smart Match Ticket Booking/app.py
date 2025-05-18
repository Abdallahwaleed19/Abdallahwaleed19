import os
from flask import Flask, render_template, redirect, url_for, request, flash, send_file, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
import qrcode
from io import BytesIO
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import joinedload
from flask_migrate import Migrate # Added Flask-Migrate import
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
# Construct an absolute path for the database
basedir = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(basedir, 'instance')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(instance_path, "app.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app, db) # Initialize Flask-Migrate

login_manager = LoginManager(app)
login_manager.login_view = 'login'  # type: ignore

# Context Processor to make current year available to all templates
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    matches = db.relationship('FootballMatch', backref='competition_info', lazy=True) # Renamed backref to avoid conflict with potential 'competition' attribute

    def __repr__(self):
        return f'<Competition {self.name}>'

class FootballMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    tickets_available = db.Column(db.Integer, nullable=False)
    bookings = db.relationship('Booking', backref='match', lazy=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    team_a_image = db.Column(db.String(255))
    team_b_image = db.Column(db.String(255))
    # Removed direct relationship here, will access competition via competition_info backref from Competition model or by querying Competition table using competition_id

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('football_match.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    paid = db.Column(db.Boolean, default=False)
    ticket_code = db.Column(db.String(100), unique=True)

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    usage_count = db.Column(db.Integer, default=0)

# Forms
class LoginForm(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=150)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email address."), Length(max=150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters long.")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match.")])
    role = SelectField('Register as:', choices=[('customer', 'Customer'), ('admin', 'System Administrator')], validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('That email is already registered. Please choose a different one or login.')

class FootballMatchForm(FlaskForm):
    competition = SelectField('Competition', validators=[DataRequired()])
    title = StringField('Match Title (e.g., Team A vs Team B)', validators=[DataRequired()], render_kw={"placeholder": "E.g., Team A vs Team B"})
    description = TextAreaField('Description', validators=[DataRequired()])
    date = StringField('Date & Time (YYYY-MM-DD HH:MM)', validators=[DataRequired()], render_kw={'class': 'flatpickr-datetime'})
    location = StringField('Location', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    tickets_available = IntegerField('Tickets Available', validators=[DataRequired()])
    team_a_image = FileField('Team A Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    team_b_image = FileField('Team B Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    submit = SubmitField('Save Match')

class BookingForm(FlaskForm):
    promotion_code = StringField('Promotion Code (optional)')
    submit = SubmitField('Book Now')

class PromotionForm(FlaskForm):
    code = StringField('Promotion Code', validators=[DataRequired(), Length(min=2, max=50)])
    discount = IntegerField('Discount (%)', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Add Promotion')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    matches = FootballMatch.query.order_by(FootballMatch.date).all()
    return render_template('index.html', matches=matches)

@app.route('/match/<int:match_id>', methods=['GET', 'POST'])
def match_detail(match_id):
    match = FootballMatch.query.get_or_404(match_id)
    form = BookingForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('Please log in to book.', 'warning')
            return redirect(url_for('login'))
        if current_user.is_admin:
            flash('Admins cannot book tickets. Please use a customer account.', 'danger')
            return redirect(url_for('index'))
        if match.tickets_available < 1:
            flash('No tickets available for this match.', 'danger')
            return redirect(url_for('index'))
        # Promotion logic
        discount = 0
        if form.promotion_code.data:
            promo = Promotion.query.filter_by(code=form.promotion_code.data).first()
            if promo:
                discount = promo.discount
                promo.usage_count += 1
                db.session.commit()
        # Mock payment
        match.tickets_available -= 1
        ticket_code = f"TICKET-M{match.id}-U{current_user.id}-{int(datetime.now(timezone.utc).timestamp())}"
        booking = Booking()
        booking.user_id = current_user.id
        booking.match_id = match.id
        booking.paid = True
        booking.ticket_code = ticket_code
        db.session.add(booking)
        db.session.commit()
        flash('Booking successful! Your ticket is ready.', 'success')
        return redirect(url_for('dashboard'))
    return render_template('match_detail.html', match=match, form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', bookings=bookings)

@app.route('/ticket/<int:booking_id>/qr')
@login_required
def ticket_qr(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != current_user.id and not current_user.is_admin:
        flash('Unauthorized.', 'danger')
        return redirect(url_for('dashboard'))
    qr = qrcode.make(booking.ticket_code)
    buf = BytesIO()
    qr.save(buf, format='PNG')
    buf.seek(0)
    if request.args.get('download') == '1':
        return send_file(
            buf,
            mimetype='image/png',
            as_attachment=True,
            download_name=f"ticket_{booking.id}_qr.png"
        )
    return send_file(buf, mimetype='image/png')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))
        flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.email.data).first()
        if existing_user:
            flash('That email is already registered. Please use a different email or login.', 'danger')
            return redirect(url_for('register'))

        user = User()
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.username = form.email.data
        user.set_password(form.password.data)
        user.is_admin = (form.role.data == 'admin')
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'info')
    return redirect(url_for('index'))

# Admin routes
@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if not current_user.is_admin:
        flash('Admins only.', 'danger')
        return redirect(url_for('index'))
    form = FootballMatchForm()
    form.competition.choices = [(c.id, c.name) for c in Competition.query.order_by('name').all()]
    if form.validate_on_submit():
        match = FootballMatch()
        match.competition_id = form.competition.data
        match.title = form.title.data
        match.description = form.description.data
        try:
            match.date = datetime.strptime(form.date.data, '%Y-%m-%d %H:%M')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD HH:MM', 'danger')
            return render_template('admin.html', matches=FootballMatch.query.order_by(FootballMatch.date).all(), form=form)
        match.location = form.location.data
        match.price = form.price.data
        match.tickets_available = form.tickets_available.data
        # Handle team images
        for team_field, attr in [(form.team_a_image, 'team_a_image'), (form.team_b_image, 'team_b_image')]:
            file = team_field.data
            if file:
                filename = secure_filename(file.filename)
                unique_filename = f"{attr}_{match.title.replace(' ', '_')}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
                setattr(match, attr, unique_filename)
        db.session.add(match)
        db.session.commit()
        flash('Football match created.', 'success')
        return redirect(url_for('admin'))
    matches = FootballMatch.query.order_by(FootballMatch.date).all()
    return render_template('admin.html', matches=matches, form=form)

@app.route('/admin/edit_match/<int:match_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_match(match_id):
    if not current_user.is_admin:
        flash('Admins only.', 'danger')
        return redirect(url_for('index'))
    match_to_edit = FootballMatch.query.get_or_404(match_id)
    form = FootballMatchForm(obj=match_to_edit)
    form.competition.choices = [(c.id, c.name) for c in Competition.query.order_by('name').all()]
    if form.validate_on_submit():
        match_to_edit.competition_id = form.competition.data
        match_to_edit.title = form.title.data
        match_to_edit.description = form.description.data
        try:
            match_to_edit.date = datetime.strptime(form.date.data, '%Y-%m-%d %H:%M')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD HH:MM', 'danger')
            form.competition.choices = [(c.id, c.name) for c in Competition.query.order_by('name').all()]
            return render_template('edit_match.html', form=form, match_id=match_id)
        match_to_edit.location = form.location.data
        match_to_edit.price = form.price.data
        match_to_edit.tickets_available = form.tickets_available.data
        # Handle team images
        for team_field, attr in [(form.team_a_image, 'team_a_image'), (form.team_b_image, 'team_b_image')]:
            file = team_field.data
            if file:
                filename = secure_filename(file.filename)
                unique_filename = f"{attr}_{match_to_edit.title.replace(' ', '_')}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
                setattr(match_to_edit, attr, unique_filename)
        db.session.commit()
        flash(f'Match "{match_to_edit.title}" updated successfully.', 'success')
        return redirect(url_for('admin'))
    elif request.method == 'GET':
        form.date.data = match_to_edit.date.strftime('%Y-%m-%d %H:%M')
        form.competition.data = match_to_edit.competition_id
    return render_template('edit_match.html', form=form, match_id=match_id)

@app.route('/admin/bookings')
@login_required
def admin_view_bookings():
    if not current_user.is_admin:
        flash('Admins only.', 'danger')
        return redirect(url_for('index'))
    
    # Query all bookings, eager load user and match details to prevent N+1 queries in template
    all_bookings = Booking.query.options(
        joinedload(Booking.user), 
        joinedload(Booking.match)
    ).order_by(Booking.timestamp.desc()).all()
    
    return render_template('admin_bookings.html', bookings=all_bookings)

@app.route('/admin/delete_match/<int:match_id>')
@login_required
def delete_match(match_id):
    if not current_user.is_admin:
        flash('Admins only.', 'danger')
        return redirect(url_for('index'))
    match = FootballMatch.query.get_or_404(match_id)
    for booking in match.bookings:
        db.session.delete(booking)
    db.session.delete(match)
    db.session.commit()
    flash('Football match and associated bookings deleted.', 'info')
    return redirect(url_for('admin'))

@app.route('/analytics')
@login_required
def analytics():
    if not current_user.is_admin:
        flash('Admins only.', 'danger')
        return redirect(url_for('index'))
    total_bookings = Booking.query.count()
    total_users = User.query.count()
    total_matches = FootballMatch.query.count()
    promo_usage = Promotion.query.all()
    return render_template('analytics.html', total_bookings=total_bookings, total_users=total_users, total_matches=total_matches, promo_usage=promo_usage)

@app.route('/admin/promotions', methods=['GET', 'POST'])
@login_required
def admin_promotions():
    if not current_user.is_admin:
        flash('Admins only.', 'danger')
        return redirect(url_for('index'))
    form = PromotionForm()
    if form.validate_on_submit():
        if Promotion.query.filter_by(code=form.code.data).first():
            flash('Promotion code already exists.', 'danger')
        else:
            promo = Promotion(code=form.code.data, discount=form.discount.data)
            db.session.add(promo)
            db.session.commit()
            flash('Promotion code added.', 'success')
        return redirect(url_for('admin_promotions'))
    promotions = Promotion.query.order_by(Promotion.id.desc()).all()
    return render_template('admin_promotions.html', form=form, promotions=promotions)

# Utility: Create admin user if not exists
def create_admin():
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
        
    # Ensure the app context is active for database operations here
    with app.app_context():
        if not User.query.filter_by(username='admin@example.com').first():
            admin = User()
            admin.first_name = 'Admin'
            admin.last_name = 'User'
            admin.username = 'admin@example.com'
            admin.set_password('admin')
            admin.is_admin = True
            db.session.add(admin)
            db.session.commit()

def seed_competitions():
    competitions_to_add = [
        "UEFA Champions League", "CAF Champions League", "Premier League", 
        "La Liga", "Egyptian Premier League", "Bundesliga", "Serie A", "Ligue 1", "Other"
    ]
    with app.app_context():
        for comp_name in competitions_to_add:
            if not Competition.query.filter_by(name=comp_name).first():
                competition = Competition(name=comp_name)
                db.session.add(competition)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        # Flask-Migrate handles database creation/updates
        seed_competitions() # Seed competitions
        create_admin() 
    app.run(debug=True) 