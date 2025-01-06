# app/routes/__init__.py
from .auth import auth_bp
from .portfolio import portfolio_bp

# You can add more Blueprints here if needed
__all__ = ['auth_bp', 'portfolio_bp']