from database import db

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    # Relacion con ventas 1-N
    sales = db.relationship('Sale', back_populates='client')

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Client.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Client.query.get(id)
    
    def update(self, name=None, email=None, phone=None):
        if name and email and phone:
            self.name = name
            self.email = email
            self.phone = phone
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        

