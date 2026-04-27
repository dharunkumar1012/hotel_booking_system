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


def room_booking(customer_name, room_id, check_in, check_out):
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
        INSERT INTO bookings(customer_name, room_id, check_in, check_out)
        VALUES(%s, %s, %s, %s)
    """
    cursor.execute(query, (customer_name, room_id, check_in, check_out))

    connection.commit()

    cursor.close()
    connection.close()

    return "Booking Successful!"
