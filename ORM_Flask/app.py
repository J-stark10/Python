from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definicion del modelo
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product {self.name}>, Price: {self.price}, Stock: {self.stock}"
    

# Funcion para inicializar la base de datos
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de Datos creada exitosamente.")

# Operaciones CRUD
# Insertar productos(manual)
def insert_products():
    with app.app_context():
        # instanciacion del producto
        product_1 = Product(name="Galletas", price=9.99, stock=100)
        product_2 = Product(name="Pan", price=19.99, stock=50)
        product_3 = Product(name="Leche", price=29.99, stock=25)

        # adición de objetos (registros en la tabla)
        db.session.add(product_1)
        db.session.add(product_2)
        db.session.add(product_3)
        # Consolida los cambios en la base de datos
        db.session.commit()
        print("Productos insertados exitosamente.")
    
# Consultas a la base de datos
def query_products():
    with app.app_context():
        # Consultar todos los productos de una tabla
        print("\nListado de productos:")
        products = Product.query.all()
        for product in products:
            print(product)

        # Consultas que cumplen una condición
        print("\nLista de productos filtrados")
        filtrados = Product.query.filter(Product.price > 10).all()
        for product in filtrados:
            print(product)  

        # Consulta de un solo producto
        print("\nObtener un solo registro")
        producto = Product.query.filter_by(id=1).first()
        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

# Actualización de un producto
def update_product():
    with app.app_context():
        print(f"\nActualizando de un producto")
        product = Product.query.filter_by(id=1).first()
        if product:
            product.price = 7.00
            product.stock = 53
            # consolida los cambios en la base de datos
            db.session.commit()
            print(f"Producto actualizado: {product}")
        else:
            print("Producto no encontrado para actualizar.")

# Eliminación de un producto
def delete_product():
    with app.app_context():
        print(f"\nEliminando un producto")
        product = Product.query.filter_by(id=2).first()
        if product:
            db.session.delete(product)
            # consolida los cambios en la base de datos
            db.session.commit()
            print(f"Producto eliminado: {product}")
        else:
            print("Producto no encontrado para eliminar.")

if __name__ == '__main__':    
    init_db()
    insert_products()
    query_products()
    update_product()
    delete_product()