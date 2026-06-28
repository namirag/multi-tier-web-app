from flask import Flask, jsonify, request  # type: ignore
import mysql.connector  # type: ignore

app = Flask(__name__)

# ---------------- CORS ----------------
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


# ---------------- DB CONNECTION ----------------
def get_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="admin123",
        database="shop",
        port=3306
    )


# ---------------- GET PRODUCTS ----------------
@app.route("/products", methods=["GET"])
def products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


# ---------------- ADD PRODUCT ----------------
@app.route("/products", methods=["POST"])
def add_product():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name) VALUES (%s)",
        (data["name"],)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "saved"})


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)