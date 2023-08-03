from extensions.database import db

class Profile(db.Model):
    
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    cep = db.Column(db.String)
    email = db.Column(db.String)
    telefone = db.Column(db.String)
    comment = db.Column(db.String)
