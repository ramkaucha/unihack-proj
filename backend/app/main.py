from flask import Flask, jsonify
from model import db
from flask_cors import CORS
import requests
import os

app = Flask(__name__)

# sqlite database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # 数据库路径
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db.init_app(app)

CORS(app)

API_URL = os.environ.get("API_URL", "http://localhost:5000")
CLIENT_URL = os.environ.get("CLIENT_URL", "http://localhost:3000")
OPEN_API = os.environ.get("OPEN_AI_API")

@app.route("/solve")
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


created = False  # Flag to check if tables have been created


# create tables only once on app startup
@app.before_request
def create_tables():
    global created
    if not created:
        db.create_all()
        created = True


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

exported_app = app
