from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return f"Welcome, {username}! You are using POST method"
    else:
        # This will show a form when the user goes to /login
        return '''
            <form method="POST" action="/login">
                <label>Username:</label><br>
                <input type="text" name="username"><br><br>
                <label>Password:</label><br>
                <input type="password" name="password"><br><br>
                <input type="submit" value="Login">
            </form>
        '''

if __name__ == "__main__":
    app.run(debug=True)
