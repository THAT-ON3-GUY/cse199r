from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    aisle INT,
    price DECIMAL(6,2)
)
""")

conn.commit()
cursor.close()
conn.close()

print("Ingredients table created")
