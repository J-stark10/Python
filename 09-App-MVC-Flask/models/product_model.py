from database import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(2,2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    # Relacion con ventas 1-N 
    sales = db.relationship('Sale', back_populates='product')

    def __init__(self, description, price, stock):
        self.description = description
        self.price = price
        self.stock = stock

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Product.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)
    
    def update(self, description, price, stock):
        if description and price and stock:
            self.description = description
            self.price = price
            self.stock = stock
        
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()