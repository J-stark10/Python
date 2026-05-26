from flask import request, redirect, url_for, Blueprint

from models.product_model import Product
from views import product_view

product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/')
def index():
    products = Product.get_all()
    return product_view.list(products)

@product_bp.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']

        product = Product(description, price, stock)
        product.save()

        return redirect(url_for('product.index'))

    return product_view.create()

@product_bp.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    product = Product.get_by_id(id)

    if request.method == 'POST':
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']

        product.update(description=description, price=price, stock=stock)

        return redirect(url_for('product.index'))

    return product_view.edit(product)

@product_bp.route('/delete/<int:id>')
def delete(id):
    product = Product.get_by_id(id)
    product.delete()
    return redirect(url_for('product.index'))
