from flask import Blueprint, render_template, request, jsonify, session
from routes.auth import login_required
from utils.ai_engine import get_openai_response

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chat')
@login_required
def chat():
    return render_template('chatbot.html')

@chatbot_bp.route('/api/chat', methods=['POST'])
@login_required
def chat_api():
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400
        
    reply = get_openai_response(message)
    return jsonify({'response': reply})
