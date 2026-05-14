from flask import Flask, redirect, render_template, request

from db import login, register, get_available_rooms, room_booking, get_bookings, cancel_booking

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

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])  # type: ignore
def register_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        result = register(username, password)
        return result

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/rooms")
def view_rooms():

    rooms = get_available_rooms()

    return render_template(
        "rooms.html",
        rooms=rooms
    )


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

    return render_template("book.html")


@app.route("/bookings")
def view_bookings():

    user_id = 1

    bookings = get_bookings(user_id)

    return render_template(
        "bookings.html",
        bookings=bookings
    )


@app.route("/cancel", methods=["GET", "POST"])
def cancel_room():
    if request.method == "POST":
        booking_id = int(request.form["booking_id"])

        # Temporary user_id
        user_id = 1

        result = cancel_booking(user_id, booking_id)

        return f"""
            <h3>{result}</h3>

            <a href="/cancel">Cancel Another Booking</a><br><br>
            <a href="/dashboard">Back to Dashboard</a>
        """

    return render_template("cancel.html")


if __name__ == "__main__":
    app.run(debug=True)
