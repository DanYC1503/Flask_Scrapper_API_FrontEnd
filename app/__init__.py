from flask import Flask

def create_app():
    app = Flask(__name__)

    
    from .routes import frontend_bp
    app.register_blueprint(frontend_bp)

    return app
