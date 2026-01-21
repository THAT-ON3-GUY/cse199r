from flask import Flask, render_template
from database import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM ingredients")
    ingredients = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", ingredients=ingredients)

if __name__ == "__main__":
    app.run(debug=True)
