from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
from app import db
from app.model.post import Post  # Import the Post model
from app.service.chatbot_service import detect_language, check_for_inappropriate_content, generate_issue_report, translate_to_english

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "").strip()
    project_id = data.get("project_id")
    user_id = data.get("user_id")
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    language = detect_language(user_input)
    conversation_history = [user_input]
    warnings = 0

    while True:
        moderation_result = check_for_inappropriate_content(user_input)
        if moderation_result != "safe":
            warnings += 1
            if warnings >= MAX_WARNINGS:
                return jsonify({"error": "Chat terminated due to inappropriate content."}), 403
            user_input = ""  # Clear input and request new message from frontend
            continue
        
        conversation_history.append(user_input)
        issue_report = generate_issue_report(conversation_history, language)
        stored_report = translate_to_english(issue_report)
        
        # Save issue report to database as a Post
        new_post = Post(
            title="Generated Issue Report",
            description=stored_report,
            project_id=project_id,
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

