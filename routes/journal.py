from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from models.db import db, Journal
from routes.auth import login_required

journal_bp = Blueprint('journal', __name__)

@journal_bp.route('/journal', methods=['GET', 'POST'])
@login_required
def journal_page():
    user_id = session.get('user_id')
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            new_entry = Journal(title=title, content=content, user_id=user_id)
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('journal.journal_page'))
    
    entries = Journal.query.filter_by(user_id=user_id).order_by(Journal.timestamp.desc()).all()
    return render_template('journal.html', entries=entries)
