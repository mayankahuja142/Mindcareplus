from flask import Flask, render_template
from config import Config
from models.db import db
from routes.auth import auth_bp
from routes.mood import mood_bp
from routes.journal import journal_bp
from routes.chatbot import chatbot_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(mood_bp)
    app.register_blueprint(journal_bp)
    app.register_blueprint(chatbot_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/breathing')
    def breathing():
        return render_template('breathing.html')

    with app.app_context():
        db.create_all()

    return app
import os

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
