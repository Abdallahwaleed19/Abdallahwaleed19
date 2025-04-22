from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from urllib.parse import urlparse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # type: ignore

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))  # admin, employee, customer

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    biography = db.Column(db.Text)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    availability = db.Column(db.Boolean, default=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref='books')

class LibraryBranch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(200))
    phone = db.Column(db.String(20))

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    role = db.Column(db.String(50))
    branch_id = db.Column(db.Integer, db.ForeignKey('library_branch.id'))
    branch = db.relationship('LibraryBranch', backref='employees')

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='customers')

class LibraryCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    active_date = db.Column(db.Date)
    expired_date = db.Column(db.Date)
    customer = db.relationship('Customer', backref='library_cards')

class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    checkout_date = db.Column(db.Date, default=datetime.now().date())
    due_date = db.Column(db.Date)
    returned = db.Column(db.Boolean, default=False)
    
    customer = db.relationship('Customer', backref='checkouts')
    book = db.relationship('Book', backref='checkouts')

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('dashboard')
            return redirect(next_page)
        flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    stats = {
        'books': Book.query.count(),
        'customers': Customer.query.count(),
        'branches': LibraryBranch.query.count(),
        'employees': Employee.query.count()
    }
    
    # Get recent checkouts for activity feed
    recent_checkouts = Checkout.query.order_by(Checkout.checkout_date.desc()).limit(5).all()
    
    recent_activities = []
    for checkout in recent_checkouts:
        activity = {
            'message': f'Book checked out: "{checkout.book.title}" by {checkout.customer.name}',
            'time_ago': f"{(datetime.now().date() - checkout.checkout_date).days} days ago"
        }
        recent_activities.append(activity)
    
    # Add some sample activities if none exist
    if not recent_activities:
        recent_activities = [
            {'message': 'New book added: "Python Programming"', 'time_ago': '2 minutes ago'},
            {'message': 'Customer registered: John Doe', 'time_ago': '15 minutes ago'},
            {'message': 'Book checked out: "Clean Code"', 'time_ago': '1 hour ago'}
        ]
    
    return render_template('dashboard.html',
                         stats=stats,
                         recent_activities=recent_activities,
                         all_branches=LibraryBranch.query.all(),
                         all_customers=Customer.query.all(),
                         available_books=Book.query.filter_by(availability=True).all())

@app.route('/add_branch', methods=['POST'])
@login_required
def add_branch():
    try:
        name = request.form['name']
        location = request.form['location']
        phone = request.form['phone']
        
        new_branch = LibraryBranch(name=name, location=location, phone=phone) # type: ignore
        db.session.add(new_branch)
        db.session.commit()
        
        flash('Branch added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding branch: {str(e)}', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/add_employee', methods=['POST'])
@login_required
def add_employee():
    try:
        name = request.form['name']
        role = request.form['role']
        branch_id = request.form['branch_id']
        
        new_employee = Employee(name=name, role=role, branch_id=branch_id) # type: ignore
        db.session.add(new_employee)
        db.session.commit()
        
        flash('Employee added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding employee: {str(e)}', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/checkout_book', methods=['POST'])
@login_required
def checkout_book():
    try:
        customer_id = request.form['customer_id']
        book_id = request.form['book_id']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d').date()
        
        # Update book availability
        book = Book.query.get(book_id)
        if not book:
            flash('Book not found', 'danger')
            return redirect(url_for('dashboard'))
        
        if not book.availability:
            flash('Book is already checked out', 'danger')
            return redirect(url_for('dashboard'))
            
        book.availability = False
        
        # Create checkout record
        new_checkout = Checkout(
            customer_id=customer_id, # type: ignore
            book_id=book_id, # type: ignore
            due_date=due_date # type: ignore
        )
        db.session.add(new_checkout)
        db.session.commit()
        
        flash('Book checked out successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error checking out book: {str(e)}', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/issue_library_card', methods=['POST'])
@login_required
def issue_library_card():
    try:
        customer_id = request.form['customer_id']
        duration = int(request.form['duration'])
        
        # Check if customer already has a card
        existing_card = LibraryCard.query.filter_by(customer_id=customer_id).first()
        if existing_card:
            flash('Customer already has a library card', 'warning')
            return redirect(url_for('dashboard'))
        
        active_date = datetime.now().date()
        expired_date = active_date + timedelta(days=duration*30)
        
        new_card = LibraryCard(
            customer_id=customer_id, # type: ignore
            active_date=active_date, # type: ignore
            expired_date=expired_date # type: ignore
        )
        db.session.add(new_card)
        db.session.commit()
        
        flash('Library card issued successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error issuing library card: {str(e)}', 'danger')
    return redirect(url_for('dashboard'))

# Book Management
@app.route('/books')
@login_required
def books():
    all_books = Book.query.all()
    return render_template('books.html', books=all_books)

@app.route('/add_book', methods=['POST'])
@login_required
def add_book():
    try:
        title = request.form['title']
        author_name = request.form['author']
        availability = True
        
        # Find or create author
        author = Author.query.filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name, biography="") # type: ignore
            db.session.add(author)
            db.session.commit()
        
        new_book = Book(title=title, author_id=author.id, availability=availability) # type: ignore
        db.session.add(new_book)
        db.session.commit()
        
        flash('Book added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding book: {str(e)}', 'danger')
    return redirect(url_for('books'))

# Customer Management
@app.route('/customers')
@login_required
def customers():
    all_customers = Customer.query.all()
    return render_template('customers.html', customers=all_customers)

@app.route('/add_customer', methods=['POST'])
@login_required
def add_customer():
    try:
        name = request.form['name']
        address = request.form['address']
        
        new_customer = Customer(name=name, address=address) # type: ignore
        db.session.add(new_customer)
        db.session.commit()
        
        flash('Customer added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding customer: {str(e)}', 'danger')
    return redirect(url_for('customers'))

# Employee Management
@app.route('/employees')
@login_required
def employees():
    all_employees = Employee.query.all()
    all_branches = LibraryBranch.query.all()
    return render_template('employees.html', employees=all_employees, branches=all_branches)

# Branch Management
@app.route('/branches')
@login_required
def branches():
    all_branches = LibraryBranch.query.all()
    return render_template('branches.html', branches=all_branches)

# Initialize database
with app.app_context():
    db.create_all()
    # Create admin user if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin', # type: ignore
            password=generate_password_hash('admin123', method='pbkdf2:sha256'), # type: ignore
            role='admin' # type: ignore
        )
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)