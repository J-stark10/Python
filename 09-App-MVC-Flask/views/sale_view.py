from flask import render_template

def list(sales):
    return render_template('sales/index.html', sales=sales)

def create(clients, products):
    # se requiere productos y clientes
    return render_template('sales/create.html', clients=clients, products=products)

def edit(sale, clients, products):
    # se requiere productos y clientes
    return render_template('sales/edit.html', sale=sale, clients=clients, products=products)