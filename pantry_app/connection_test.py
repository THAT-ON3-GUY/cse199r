import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nitro4321!",
        database="pantry_app"
    )
    print("Connected!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
