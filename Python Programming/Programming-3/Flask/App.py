from flask import * 
from flask import render_template
section_test = Flask(__name__)
@section_test.route("/")
def homepage():
    return render_template("home.html")
if __name__ == "__main__":
    section_test.run(debug=True)