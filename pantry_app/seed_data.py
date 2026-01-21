from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO ingredients (name, aisle, price) VALUES (%s, %s, %s)",
    ("Flour", 8, 3.29)
)
cursor.execute(
    "INSERT INTO ingredients (name, aisle, price) VALUES (%s, %s, %s)",
    ("Eggs", 3, 4.19)
)

conn.commit()
cursor.close()
conn.close()

print("Test data inserted!")
