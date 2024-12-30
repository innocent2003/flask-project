from flask import Flask
from app.controllers.auth_controller import auth_bp
from app.controllers.user_controller import user_bp

def create_app(template_folder=None):
    app = Flask(__name__, template_folder=template_folder or 'templates')
    app.secret_key = 'your_secret_key_here'

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)

    return app
