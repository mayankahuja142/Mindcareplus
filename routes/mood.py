from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from models.db import db, Mood
from routes.auth import login_required

mood_bp = Blueprint('mood', __name__)

# 😔 😕 😐 🙂 😄
@mood_bp.route('/dashboard')
@login_required
def dashboard():
    user_id = session.get('user_id')
    moods = Mood.query.filter_by(user_id=user_id).order_by(Mood.timestamp.desc()).limit(7).all()
    avg_mood = "N/A"
    
    emoji_map = {1: '😔', 2: '😕', 3: '😐', 4: '🙂', 5: '😄'}
    parsed_moods = [{'value': m.value, 'emoji': emoji_map.get(m.value, ''), 'time': m.timestamp.strftime('%b %d')} for m in moods]
    
    if moods:
        avg_mood = round(sum(m.value for m in moods) / len(moods), 1)
    
    return render_template('dashboard.html', avg_mood=avg_mood, recent_moods=parsed_moods)

@mood_bp.route('/api/mood', methods=['POST'])
@login_required
def add_mood():
    data = request.get_json()
    value = data.get('value')
    if value and 1 <= int(value) <= 5:
        mood = Mood(value=int(value), user_id=session.get('user_id'))
        db.session.add(mood)
        db.session.commit()
        return jsonify({'success': True}), 200
    return jsonify({'error': 'Invalid mood value'}), 400

@mood_bp.route('/api/mood/chart', methods=['GET'])
@login_required
def mood_chart_data():
    user_id = session.get('user_id')
    # Get all moods sorted by time
    moods = Mood.query.filter_by(user_id=user_id).order_by(Mood.timestamp.asc()).all()
    labels = [m.timestamp.strftime('%a %I:%M %p') for m in moods]
    values = [m.value for m in moods]
    return jsonify({'labels': labels, 'values': values})
