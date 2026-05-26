from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)
        self.role = role

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    def update(self, name, username, password, role):
        if name: 
            self.name = name
        if username:
            self.username = username
        if password: 
            self.password = self.hash_password(password)
        if role: 
            self.role = role
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()