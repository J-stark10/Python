from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///biblioteca.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Declaración para usar SQLAlchemy
db = SQLAlchemy(app)

# Tabla intermedia
libro_genero = db.Table(
    'libro_genero',
    db.Column("libro_id", db.Integer, db.ForeignKey("libros.id"),primary_key=True),
    db.Column("genero_id",db.Integer, db.ForeignKey("generos.id"),primary_key=True)
)

# Crear modelo 1 - N (AUTOR - LIBRO)
class Autor(db.Model):
    __tablename__ = "autores"

    id = db.Column(db.Integer,primary_key= True)
    nombre = db.Column(db.String(100), nullable=False)
    nacionalidad = db.Column(db.String(100))

    libros = db.relationship("Libro", back_populates="autor", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Autor > nombre: {self.nombre} - nacionalidad: {self.nacionalidad}"
    
class Libro(db.Model):
    __tablename__ = "libros"

    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(200), nullable = False)
    anio = db.Column(db.Integer)

    autor_id = db.Column(db.Integer, db.ForeignKey("autores.id"), nullable=False)
    generos = db.relationship('Genero',secondary=libro_genero, back_populates="libros")

    autor = db.relationship("Autor", back_populates="libros")
    
    def __repr__(self):
        return f"Libro > titulo: {self.titulo} - anio {self.anio}"

class Genero(db.Model):
    __tablename__ = "generos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50),nullable=False)

    libros = db.relationship("Libro",secondary=libro_genero, back_populates="generos")

    def __repr__(self):
        return f"Genero > nombre:{self.nombre}"

# REQUERIMIENTOS:  
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de Datos inicializada correctamente")

def insertar_datos(): 
    with app.app_context():
        
        genero1 = Genero(nombre='Programación')
        genero2 = Genero(nombre="Bases de Datos")
        genero3 = Genero(nombre="Redes")
        genero4 = Genero(nombre="Ingeniería de Software")

        autor1 = Autor(nombre="Carlos Mendoza", nacionalidad="Bolivia")
        autor2 = Autor(nombre="Luis Ramírez", nacionalidad="Perú")
        autor3 = Autor(nombre="Ana Torres", nacionalidad="Colombia")

        libro1 = Libro(titulo="Introducción a la Programación", anio=2021, autor=autor1)
        libro2 = Libro(titulo="Python desde Cero", anio=2020, autor=autor1)
        libro3 = Libro(titulo="Modelado de Bases de Datos", anio=2019, autor=autor2)
        libro4 = Libro(titulo="Administración de SQL Server", anio=2018, autor=autor2)
        libro5 = Libro(titulo="Arquitectura de Software", anio=2022, autor=autor3)

        libro1.generos.append(genero1)
        libro2.generos.append(genero1)
        libro3.generos.extend([genero2])
        libro4.generos.extend([genero2, genero3])
        libro5.generos.extend([genero4, genero1])

        db.session.add_all([genero1, genero2, genero3, genero4,
                            autor1, autor2, autor3,
                            libro1, libro2, libro3, libro4, libro5])
        db.session.commit()
        print("Datos insertados correctamente")

def consultar_datos():
    with app.app_context():
        print('\n---------Autores con sus libros--------')
        autores = Autor.query.all()
        for autor in autores:
            print(f"\nAutor: '{autor.nombre}' sus libros son : ")
            for libro in autor.libros:
                print(f"- Titulo: '{libro.titulo}' Año: '{libro.anio}'")
        
        print('\n---------Generos con sus libros----------')
        generos = Genero.query.all()
        for genero in generos:
            print(f"\nGenero: '{genero.nombre}' tiene los libros: ")
            for libro in genero.libros:
                print(f"- Titulo: '{libro.titulo}' Año: '{libro.anio}'")

def actualizar_datos():
    with app.app_context():
        print('\n Actualizar el titulo de un libro')
        libro = Libro.query.filter_by(id=4).first()
        if libro: 
            libro.titulo = "Bases de Datos"
            db.session.commit()
            print("Titulo de libro actualizado")
        else:
            print("Libro no encontrado")

def eliminar_datos():
    with app.app_context():
        print('\nEliminar un autor')
        autor = Autor.query.filter_by(id=1).first()
        if autor:
            db.session.delete(autor)
            db.session.commit()
            print("Autor eliminado correctamente")
        else:
            print("Autor no encontrado")

if __name__ == "__main__":
    # init_db()
    # insertar_datos()
    consultar_datos()
    # actualizar_datos()
    #eliminar_datos()
