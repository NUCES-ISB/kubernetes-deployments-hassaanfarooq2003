from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_NAME = os.getenv("POSTGRES_DB", "flaskdb")
DB_USER = os.getenv("POSTGRES_USER", "flaskuser")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = "postgres-service"
DB_PORT = "5432"

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

@app.route('/')
def index():
    conn = connect_db()
    if conn:
        return jsonify({"message": "Connected to PostgreSQL successfully!"})
    return jsonify({"message": "Failed to connect to PostgreSQL"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
