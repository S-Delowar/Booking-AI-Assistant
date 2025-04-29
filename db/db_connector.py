import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")


def get_connection():
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )


def check_connection():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Connected to: {db_version[0]}")
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    check_connection()