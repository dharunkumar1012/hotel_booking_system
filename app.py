from flask import Flask, redirect, request

from db import login, register, get_available_rooms, room_booking

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


@app.route("/rooms")
def view_rooms():
    rooms = get_available_rooms()
    output = "<h2>Available Rooms</h2>"

    for room in rooms:  # type: ignore
        output += f"""
            <p>
            Room ID: {room[0]}<br>
            Type: {room[1]}<br>
            Capacity: {room[2]}<br>
            Price: ₹{room[3]}
            </p>
            <hr>
        """

    output += '<a href="/dashboard">Back to Dashboard</a>'
    return output


@app.route("/book", methods=["GET", "POST"])
def book_room():
    if request.method == "POST":
        customer_name = request.form["customer_name"]
        room_id = int(request.form["room_id"])
        check_in = request.form["check_in"]
        check_out = request.form["check_out"]

        user_id = 1
        result = room_booking(
            user_id,
            customer_name,
            room_id,
            check_in,
            check_out
        )

        return f"""
            <h3>{result}</h3>

            <a href="/book">Book Another Room</a><br><br>
            <a href="/dashboard">Back to Dashboard</a>
        """

    return """
         <h2>Book Room</h2>

        <form method="POST">

            Name:
            <input type="text" name="customer_name"><br><br>

            Room ID:
            <input type="number" name="room_id"><br><br>

            Check In:
            <input type="date" name="check_in"><br><br>

            Check Out:
            <input type="date" name="check_out"><br><br>

            <button type="submit">Book Room</button>

        </form>

        <br>
        <a href="/dashboard">Back to Dashboard</a>
"""


if __name__ == "__main__":
    app.run(debug=True)
