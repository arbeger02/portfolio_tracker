# app/utils/auth.py
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def hash_password(password):
    """Hash a password using bcrypt."""
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(hashed_password, password):
    """Check if a password matches the hashed password."""
    return bcrypt.check_password_hash(hashed_password, password)