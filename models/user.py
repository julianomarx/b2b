from extensions.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    categoria = db.Column(db.Integer)

    def __init__(self, name=None, email=None, password=None, categoria=None):
        if name:
            self.name = name
            self.email = email
            self.categoria = categoria
            self.password = generate_password_hash(password)
            self.is_admin = self.categoria == 1

    def verify_password(self, pwd):
        print('verificacao de senha:', check_password_hash(self.password, pwd))
        return check_password_hash(self.password, pwd)