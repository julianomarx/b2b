from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class init_app:

    def __init__(self, app):

        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///b2b.sqlite3"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SECRET_KEY'] = "ABCDEF"
        
        with app.app_context():
            db.init_app(app)
            db.create_all()
            

  
            
