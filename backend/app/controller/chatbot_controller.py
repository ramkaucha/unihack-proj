from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
from backend.app import db
from backend.app.model.post import Post  # Import the Post model
from backend.app.service.chatbot_service import detect_language, check_for_inappropriate_content, generate_issue_report, \
    translate_to_english

chatbot_bp = Blueprint('chatbot', __name__)


@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    if not request.is_json:  # Ensure request is JSON
        return jsonify({"error": "Unsupported Media Type. Use 'Content-Type: application/json'"}), 415

    data = request.get_json()  # Parse JSON safely
    user_input = data.get("message", "").strip()
    user_id = data.get("user_id")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    language = detect_language(user_input)
    moderation_result = check_for_inappropriate_content(user_input)
    if moderation_result != "safe":
        return jsonify({"error": "Input contains inappropriate content."}), 403

    issue_report = generate_issue_report(user_input, language)
    stored_report = translate_to_english(issue_report)

    # Save issue report to database as a Post
    new_post = Post(
        title="Generated Issue Report",
        description=stored_report,
        user_id=user_id,
        create_time=datetime.now(timezone.utc)
    )
    try:
        db.session.add(new_post)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)}"}), 500

    return jsonify({
        "message": "Report successfully generated and saved.",
        "post_id": new_post.post_id,
        "language": language,
        "issue_report": stored_report
    })
