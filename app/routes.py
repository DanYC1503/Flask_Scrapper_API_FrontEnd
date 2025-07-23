from flask import Blueprint, render_template

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
def home():
    return render_template('index.html')

@frontend_bp.route('/comments.html')
def comments():
    return render_template('comments.html')

@frontend_bp.route('/analytics.html')
def analytics():
    return render_template('analytics.html')