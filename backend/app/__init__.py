from flask import Flask
from app.models import db
from app.routes.chatbot_routes import chatbot_bp  # Import chatbot routes

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chatbot.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register chatbot blueprint
    app.register_blueprint(chatbot_bp, url_prefix="/api")

    return app
