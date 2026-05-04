from flask import Flask, redirect, request

from db import login, register

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])  # type: ignore
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = login(username, password)

        if user_id:
            return redirect("/dashboard")
        else:
            return "Invalid credentials"

    return """
        <h2>Login</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <button type="submit">Login</button>
        </form>
        
        <br>
        <a href="/register">Create new account</a>
    """


@app.route("/register", methods=["GET", "POST"])  # type: ignore
def register_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        result = register(username, password)
        return result

    return """
         <h2>Register</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <button type="submit">Register</button>
        </form>

        <br>
        <a href="/">Back to login</a>
"""


@app.route("/dashboard")
def dashboard():
    return """
         <h2>DK HOTEL</h2>

        <a href="/rooms">View Rooms</a><br><br>
        <a href="/book">Book Room</a><br><br>
        <a href="/bookings">View Bookings</a><br><br>
        <a href="/cancel">Cancel Booking</a><br><br>
"""


if __name__ == "__main__":
    app.run(debug=True)
