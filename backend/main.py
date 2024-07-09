from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("PGHOST"),
        database=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD")
    )
    return conn

@app.route('/submit', methods=['POST'])
def submit():
    value1 = request.json.get('value1')
    value2 = request.json.get('value2')
    if not value1 or not value2:
        logging.error("Missing values")
        return jsonify({"error": "Missing values"}), 400
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO data (value1, value2) VALUES (%s, %s)', (value1, value2))
        conn.commit()
        cur.close()
        conn.close()
        logging.info("Data submitted successfully")
        return jsonify({"message": "Data submitted successfully"}), 200
    except Exception as e:
        logging.error("Error inserting data: %s", e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port=5000)
