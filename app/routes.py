from flask import Blueprint, render_template

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
def home():
    """Página de inicio que explica la aplicación"""
    return render_template('index.html')

@frontend_bp.route('/scraping.html')
def scraping():
    """Página con el formulario de scraping"""
    return render_template('scraping.html')

@frontend_bp.route('/comments.html')
def comments():
    """Página que muestra los comentarios analizados"""
    return render_template('comments.html')

@frontend_bp.route('/analytics.html')
def analytics():
    """Página que muestra los análisis y gráficos"""
    return render_template('analytics.html')