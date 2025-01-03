from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        # Register routes
        from .routes.auth import auth_bp
        from .routes.portfolio import portfolio_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(portfolio_bp)

        # Create database tables
        db.create_all()

    return app