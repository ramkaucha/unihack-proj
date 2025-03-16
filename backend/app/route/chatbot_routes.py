from flask import Blueprint, request, jsonify
from app import db
from app.models.post import Post
from app.controller.chatbot import detect_language, generate_issue_report
from datetime import datetime, timezone

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    """Handles chat input but does not store intermediate messages."""
    data = request.json
    session_id = data.get("session_id")
    user_input = data.get("text", "").strip()

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Detect language
    language = detect_language(user_input)

    return jsonify({"status": "ongoing", "message": "✅ Continue your conversation and finalize when ready.", "language": language})

@chatbot_bp.route('/finalize', methods=['POST'])
def finalize():
    """Finalizes and stores the chatbot report as a Post."""
    data = request.json
    session_id = data.get("session_id")
    user_id = data.get("user_id")  # Ensure frontend sends user_id
    project_id = data.get("project_id")  # The project this post belongs to
    conversation_history = data.get("conversation_history", [])

    if not conversation_history:
        return jsonify({"error": "No conversation history provided"}), 400

    # Detect language from the first message
    language = detect_language(conversation_history[0])

    # Generate final structured report
    final_report = generate_issue_report(conversation_history, language)

    # Save as a Post in the database
    new_post = Post(
        user_id=user_id,
        project_id=project_id,
        title="Chatbot Generated Report",
        description=final_report,  # Store the chatbot response in the post description
        create_time=datetime.now(timezone.utc)
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({
        "status": "finalized",
        "message": "✅ Report saved as a post.",
        "post_id": new_post.post_id,
        "title": new_post.title,
        "description": new_post.description
    })
