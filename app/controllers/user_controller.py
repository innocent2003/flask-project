from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session
from app.models import User

user_bp = Blueprint('user', __name__)

@user_bp.before_request
def check_login():
    if 'user_id' not in session and request.endpoint != 'auth.login':
        return redirect(url_for('auth.login'))

@user_bp.route('/users', methods=['GET'])
def view_users():
    users = User.all()
    return render_template('users.html', users=users)

@user_bp.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        User.create(name, email, password)
        return redirect(url_for('user.view_users'))
    return render_template('create_user.html')

@user_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        User.update(user_id, name, email, password)
        return redirect(url_for('user.view_users'))
    user = User.find_by_id(user_id)
    return render_template('edit_user.html', user=user)

@user_bp.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    User.delete(user_id)
    return redirect(url_for('user.view_users'))
