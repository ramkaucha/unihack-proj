from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)

CORS(app)

API_URL = os.environ.get("API_URL", "http://localhost:5000")
CLIENT_URL = os.environ.get("CLIENT_URL", "http://localhost:3000")

@app.route("/")
def read_root():
    return jsonify({
        "message": "Hello World"
    })

@app.route("/env-check")
def check_environment():
    return jsonify({
        "api_url": API_URL,
        "client_url": CLIENT_URL
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
