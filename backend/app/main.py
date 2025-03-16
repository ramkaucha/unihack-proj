from flask import Flask, jsonify
from model import db
from flask_cors import CORS
import requests
import os
import backend.app.route.comment_route as comment_route
import backend.app.route.post_route as post_route
import backend.app.route.project_route as project_route
import backend.app.route.user_route as user_route
from backend.app.controller.chatbot_controller import chatbot_bp


app = Flask(__name__)

app.register_blueprint(comment_route.comment_bp, url_prefix="/comments")
app.register_blueprint(post_route.post_bp, url_prefix="/posts")
app.register_blueprint(project_route.project_bp, url_prefix="/projects")
app.register_blueprint(user_route.user_bp)
app.register_blueprint(chatbot_bp)

# sqlite database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db.init_app(app)

CORS(app)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

exported_app = app
