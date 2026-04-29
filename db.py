import pymysql as py
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():
    connection = py.connect(
        host=os.getenv("DB_HOST") or "",
        user=os.getenv("DB_USER") or "",
        password=os.getenv("DB_PASSWORD") or "",
        database=os.getenv("DB_NAME") or ""
    )

    return connection


def get_available_rooms():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM rooms WHERE is_available = true ")
    rooms = cursor.fetchall()

    cursor.close()
    connection.close()

    return rooms


def room_booking(user_id, customer_name, room_id, check_in, check_out):
    connection = get_connection()
    cursor = connection.cursor()

    # STEP 1: Check if room exists
    cursor.execute("SELECT * FROM rooms WHERE room_id = %s", (room_id))
    room = cursor.fetchone()

    if not room:
        cursor.close()
        connection.close()
        return "\nRoom does not exist"

    # STEP 2: Insert booking (only if valid)
    query = """
        INSERT INTO bookings(user_id, customer_name, room_id, check_in, check_out)
        VALUES(%s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, customer_name,
                   room_id, check_in, check_out))

    connection.commit()

    cursor.close()
    connection.close()

    return "Booking Successful!"


def get_bookings(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM bookings WHERE user_id = %s", user_id,)
    bookings = cursor.fetchall()

    cursor.close()
    connection.close()

    return bookings


def cancel_booking(user_id, booking_id):
    connection = get_connection()
    cursor = connection.cursor()

    # Step 1: Check if booking exists
    cursor.execute(
        "SELECT * FROM bookings WHERE booking_id = %s AND user_id = %s", (booking_id, user_id))
    booking = cursor.fetchone()

    if not booking:
        cursor.close()
        connection.close()
        return "\nBooking not found or not authorized."

    # Step 2: Delete booking:

    query = "DELETE FROM bookings WHERE booking_id = %s"
    cursor.execute(query, (booking_id,))
    connection.commit()

    cursor.close()
    connection.close()

    return "Booking cancelled successfully!"


def login(user_name, user_password):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT * FROM users
        WHERE user_name = %s AND user_password =%s
    """
    cursor.execute(query, (user_name, user_password))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:  # type: ignore
        return user[0]  # type: ignore
    else:
        return None  # type: ignore

def register(user_name, user_password):
    connection = get_connection()
    cursor = connection.cursor()
    
    # Check if the user_name exists
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_name,))
    
    user = cursor.fetchone()
    
    if user:
        cursor.close()
        connection.close()
        return "User already exists"
    
    # Insert new user
    cursor.execute("Insert INTO users(user_name, user_password) VALUES(%s, %s),", (user_name, user_password))
    
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return "User registered successfully!"