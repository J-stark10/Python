from flask import request, redirect, url_for, Blueprint

from models.user_model import User
from views import user_view

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/')
def index():
    users = User.get_all()
    return user_view.list(users) 

@user_bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        user = User(name, username, password, role)
        user.save()

        return redirect(url_for('user.index'))

    return user_view.create()

@user_bp.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    user = User.get_by_id(id)

    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        user.update(name=name, username=username, password=password, role=role)

        return redirect(url_for('user.index'))
    
    return user_view.edit(user)

@user_bp.route('/delete/<int:id>')
def delete(id):
    user = User.get_by_id(id)
    user.delete()
    return redirect(url_for('user.index'))


