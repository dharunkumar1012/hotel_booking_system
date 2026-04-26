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
