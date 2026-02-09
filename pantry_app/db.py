import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nitro4321!",
        database="pantry_app"
    )
