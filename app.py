from flask import Flask
from extensions import database
from blueprints.loginpage import login_bp
from extensions.auth import login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KJHKJHKJH'
database.init_app(app)
login_manager.init_app(app)

login_bp.init_app(app)


@app.route("/")
def home():
    return "<h1>Something is running...</h1>"

