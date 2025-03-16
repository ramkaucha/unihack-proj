from flask import Flask, jsonify
from model import db
from flask_cors import CORS
import requests
import os
from route.user_route import user_routes

app = Flask(__name__)

# sqlite database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # 数据库路径
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db.init_app(app)


API_URL = os.environ.get("API_URL", "http://localhost:5000")
CLIENT_URL = os.environ.get("CLIENT_URL", "http://localhost:3000")

# CORS(app, resources={r"/*": {"origins": CLIENT_URL}})

CORS(app, resources={
    r"/*": {"origins": CLIENT_URL},
    r"/user/*": {"origins": CLIENT_URL, "methods": ["GET", "POST", "OPTIONS"]}
}, supports_credentials=True)

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

@app.route("/debug/routes")
def list_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            "endpoint": rule.endpoint,
            "methods": [method for method in rule.methods if method != 'OPTIONS' and method != 'HEAD'],
            "path": str(rule)
        })
    return jsonify(routes)


created = False  # Flag to check if tables have been created


# create tables only once on app startup
@app.before_request
def create_tables():
    global created
    if not created:
        db.create_all()
        created = True

app.register_blueprint(user_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

exported_app = app
