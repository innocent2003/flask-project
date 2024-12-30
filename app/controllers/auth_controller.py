from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import User
from werkzeug.security import check_password_hash

auth_bp = Blueprint(
    'auth', __name__, template_folder='../../templates'
)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.find_by_email(email)
        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            return redirect(url_for('user.view_users'))
        return redirect(url_for('auth.login'))
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))
