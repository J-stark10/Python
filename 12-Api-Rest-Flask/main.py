from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///peliculas.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pelicula(db.Model):
    __tablename__ = "peliculas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    calificacion = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "calificacion": self.calificacion
        }
    
@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a tus noches de Peliculas!!!"})

# Obtener todas las peliculas
@app.route('/peliculas', methods=['GET'])
def get_movies():
    peliculas = Pelicula.query.all()
    return jsonify([pelicula.to_dict() for pelicula in peliculas])

# Obtener una pelicula en formato JSON a partir de el id
@app.route('/peliculas/<int:id>', methods=['GET'])
def get_movie(id):
    pelicula = Pelicula.query.filter_by(id=id).first()
    if pelicula:
        return jsonify([pelicula.to_dict()])
    else:
        return jsonify({"error": "No existe la pelicula solicitada"})
    
# Adicionar un pelicula
@app.route('/peliculas', methods=['POST'])
def create_movie():
    data = request.get_json()
    pelicula = Pelicula(
        titulo = data["titulo"], 
        genero = data["genero"],
        calificacion = data["calificacion"] 
    )
    db.session.add(pelicula)
    db.session.commit()
    return jsonify(pelicula.to_dict())

# Actualizar pelicula
@app.route('/peliculas/<int:id>', methods=['PUT'])
def update_movie(id):
    data = request.get_json()
    pelicula = Pelicula.query.filter_by(id=id).first()
    if pelicula : 
        pelicula.titulo = data.get("titulo")
        pelicula.genero = data.get("genero")
        pelicula.calificacion = data.get("calificacion")

        db.session.commit()
        return jsonify(pelicula.to_dict())
    else : 
        return jsonify({"error": "No existe la pelicula solicitada"})

# Eliminar pelicula
@app.route('/peliculas/<int:id>', methods=['DELETE'])
def delete_movie(id):
    pelicula = Pelicula.query.filter_by(id=id).first()
    if pelicula:
        db.session.delete(pelicula)
        db.session.commit()
        return jsonify({"message": "Pelicula Eliminada"})
    else: 
        return jsonify({"error": "No existe la pelicula solicitada"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)