from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection

app = Flask(__name__)

@app.route("/ingredients")
def ingredients():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT ingredient_id, ingredient_name
        FROM ingredients
        ORDER BY ingredient_name;
    """)

    ingredients = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("ingredients.html", ingredients=ingredients)

@app.route("/ingredients/add", methods=["POST"])
def add_ingredient():
    name = request.form["ingredient_name"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ingredients (name, aisles_aisle_id) VALUES (%s, %s)",
        (name, 1)  # temporary aisle_id
    )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("ingredients"))

@app.route("/ingredients/delete/<int:id>", methods=["POST"])
def delete_ingredient(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ingredients WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("ingredients"))

if __name__ == "__main__":
    app.run(debug=True)
