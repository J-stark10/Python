from flask import render_template

def list(products):
    return render_template('products/index.html', products=products)

def create():
    return render_template('products/create.html')

def edit(product):
    return render_template('products/edit.html', product=product)