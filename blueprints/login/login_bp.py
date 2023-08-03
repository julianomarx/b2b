from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from models.user import User
from flask_login import login_user, current_user
from extensions.database import db
from blueprints.calendars.calendars import DataToCalendar
login_bp = Blueprint('login_bp', __name__, template_folder='templates')

def init_app(app):
    app.register_blueprint(login_bp)

controle_de_acesso = {
    1: 'admin.html',
    2: 'user.html'
}

@login_bp.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        pwd = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login_bp.login'))

        login_user(user)
        
        print(current_user)

        return redirect(url_for('login_bp.home', categoria=user.categoria))

    return render_template('login_page.html')

@login_bp.route('/register', methods=['GET', 'POST'])
def register():

    #Falta implementar tratamentos de erros na hora da inserção ao banco.

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if name and email and password:

            user = User(name, email, password)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('login_bp.login'))
        
    return render_template('register.html')

@login_bp.route('/home/<int:categoria>')
@login_required
def home(categoria):
    
    template = controle_de_acesso[int(current_user.categoria)]

    data_calendar = DataToCalendar(2023, 8).data
    return render_template(template, data_calendar=data_calendar)


