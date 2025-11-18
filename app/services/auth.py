from app.models.db import db

class AuthService:

    @staticmethod
    def authenticate(username, password):
        q = "SELECT * FROM users WHERE username=%s AND password=%s"
        result = db.execute(q, (username, password)).fetchone()
        return result
