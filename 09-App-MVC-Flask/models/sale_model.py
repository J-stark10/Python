from database import db

class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    # Especificar la relacion
    client = db.relationship('Client', back_populates='sales')
    product = db.relationship('Product', back_populates='sales')

    def __init__(self, client_id, product_id, amount, date):
        self.client_id = client_id
        self.product_id = product_id
        self.amount = amount
        self.date = date
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():  
        return Sale.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Sale.query.get(id)
    
    def update(self, client_id, product_id, amount, date):
        if client_id and product_id and amount and date:
            self.client_id = client_id
            self.product_id = product_id
            self.amount = amount
            self.date = date

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
