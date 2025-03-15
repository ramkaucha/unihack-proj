import openai
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Allows Next.js to access Flask API

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chatbot.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# OpenAI API Key
openai.api_key = "your-api-key-here"

MAX_WARNINGS = 3  # Max warnings before chat termination

# Define SQLite model for storing chat history
class ChatSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False)
    user_message = db.Column(db.Text, nullable=False)
    bot_response = db.Column(db.Text, nullable=False)
    warnings = db.Column(db.Integer, default=0)
    finalized = db.Column(db.Boolean, default=False)

# Initialize database
with app.app_context():
    db.create_all()

def detect_language(text):
    """Detects the language of the input text."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Detect the language and respond only with the language name."},
                  {"role": "user", "content": text}],
        temperature=0
    )
    return response["choices"][0]["message"]["content"].strip()

def check_for_inappropriate_content(text):
    """Detects if the text contains violence, hate speech, or sexual harassment."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Check if this text contains violence, hate speech, or sexual harassment. Respond with 'safe' or 'inappropriate'."},
                  {"role": "user", "content": text}],
        temperature=0
    )
    return response["choices"][0]["message"]["content"].strip().lower()

def translate_warning(language):
    """Translates the warning message into the user's language."""
    warning_message = "Warning: Your input contains inappropriate content (violence, hate speech, or sexual harassment). Please rephrase."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": f"Translate this into {language}: {warning_message}"}],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"].strip()

def generate_issue_report(conversation_history, language):
    """Creates a structured issue report based on the conversation history."""
    full_input = "\n".join(conversation_history)
    prompt = f"Convert this into a structured issue report in {language}:\n\n{full_input}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Create a structured issue report for developers."},
                  {"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"].strip()

def translate_to_english(text):
    """Translates structured report to English for storage."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Translate this issue report into English."},
                  {"role": "user", "content": text}],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"].strip()

@app.route('/chat', methods=['POST'])
def chat():
    """Handles chat requests and stores data in SQLite."""
    data = request.json
    session_id = data.get("session_id")
    user_input = data.get("text", "").strip()

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Get session from DB or create new
    session = ChatSession.query.filter_by(session_id=session_id).first()
    if not session:
        session = ChatSession(session_id=session_id, warnings=0)
        db.session.add(session)
        db.session.commit()

    # Detect language
    language = detect_language(user_input)

    # Check for inappropriate content
    moderation_result = check_for_inappropriate_content(user_input)
    if moderation_result != "safe":
        session.warnings += 1
        db.session.commit()

        warning_message = translate_warning(language)
        if session.warnings >= MAX_WARNINGS:
            return jsonify({"status": "terminated", "message": "🚫 Chat ended due to multiple violations.", "tag_user": True})

        return jsonify({"status": "warning", "message": f"⚠️ {warning_message} ({session.warnings}/{MAX_WARNINGS})"})

    # Generate structured report
    bot_response = generate_issue_report([user_input], language)

    # Save chat message to database
    session.user_message = user_input
    session.bot_response = bot_response
    db.session.commit()

    return jsonify({"status": "ongoing", "message": bot_response, "language": language})

@app.route('/finalize', methods=['POST'])
def finalize():
    """Finalizes the report and stores it in SQLite."""
    data = request.json
    session_id = data.get("session_id")

    session = ChatSession.query.filter_by(session_id=session_id).first()
    if not session:
        return jsonify({"error": "Invalid session"}), 400

    # Translate final report to English
    stored_report = translate_to_english(session.bot_response)

    session.finalized = True
    db.session.commit()

    return jsonify({"status": "finalized", "message": "✅ Report finalized and stored.", "stored_report": stored_report})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
