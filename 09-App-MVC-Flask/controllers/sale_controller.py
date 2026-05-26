from flask import request, redirect, url_for, Blueprint
from datetime import datetime

from models.sale_model import Sale
from models.product_model import Product
from models.client_model import Client
from views import sale_view

sale_bp = Blueprint('sale', __name__, url_prefix=('/sales'))

@sale_bp.route('/')
def index():
    sales = Sale.get_all()
    return sale_view.list(sales)

@sale_bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        client_id = request.form['client_id']
        product_id = request.form['product_id']
        amount = request.form['amount']
        date_str = request.form['date']
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        sale = Sale(client_id, product_id, amount, date)
        sale.save()
        return redirect(url_for('sale.index'))
    
    clients = Client.get_all()
    products = Product.get_all()

    return sale_view.create(clients,products)

@sale_bp.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    sale = Sale.get_by_id(id)
    if request.method == 'POST':
        client_id = request.form['client_id']
        product_id = request.form['product_id']
        amount = request.form['amount']
        date_str = request.form['date']
        date = datetime.strptime(date_str,'%Y-%m-%d').date()

        sale.update(client_id=client_id, product_id=product_id, amount=amount, date=date)
        return redirect(url_for('sale.index'))

    clients = Client.get_all()
    products = Product.get_all()

    return sale_view.edit(sale, clients, products)

@sale_bp.route('/delete/<int:id>')
def delete(id):
    sale = Sale.get_by_id(id)
    sale.delete()
    return redirect(url_for('sale.index'))
    