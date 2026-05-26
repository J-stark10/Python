from flask import request, redirect, url_for, Blueprint

from models.client_model import Client
from views import client_view

client_bp = Blueprint('client', __name__, url_prefix='/clients')

@client_bp.route('/')
def index():
    clients = Client.get_all()
    return client_view.list(clients)

@client_bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        client = Client(name, email, phone)
        client.save()

        return redirect(url_for('client.index'))

    return client_view.create()

@client_bp.route('/update/<int:id>', methods=['GET','POST'])
def edit(id):
    client = Client.get_by_id(id)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        client.update(name=name, email=email, phone=phone)
        
        return redirect(url_for('client.index'))

    return client_view.edit(client)

@client_bp.route('/delete/<int:id>')
def delete(id):
    client = Client.get_by_id(id)
    client.delete()
    return redirect(url_for('client.index')) 