import sqlite3

conn = sqlite3.connect("db_instituto.db")

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS cursos (
        id INTEGER PRIMARY KEY,
        descripcion TEXT NOT NULL,
        horas INTEGER NOT NULL
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        fecha_nacimiento DATE NOT NULL
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS inscripciones (
        id INTEGER PRIMARY KEY,
        fecha TEXT NOT NULL,
        curso_id INTEGER NOT NULL,
        estudiante_id INTEGER NOT NULL,
        FOREIGN KEY (curso_id) REFERENCES cursos(id),
        FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
    )
    """
)

# conn.execute(
#     """
#     INSERT INTO cursos(descripcion,horas)
#     VALUES ('Typescript de 0 a experto',15)
#     """
# )

# conn.execute(
#     """
#     INSERT INTO estudiantes(nombre,apellidos,fecha_nacimiento)
#     VALUES ('Jose','Quispe','2004-08-04')
#     """
# )

# conn.execute(
#     """
#     INSERT INTO inscripciones(fecha,curso_id,estudiante_id)
#     VALUES ('2024-08-31',1,1)
#     """
# )

# conn.commit()

print("\nCURSOS")
cursor = conn.execute("SELECT * FROM cursos")
for row in cursor:
    print(row)

print("\nESTUDIANTES")
cursor = conn.execute("SELECT * FROM estudiantes")
for row in cursor:
    print(row)
    
print("\nINSCRIPCIONES")
cursor = conn.execute("SELECT * FROM inscripciones")
for row in cursor:
    print(row)

























# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def inicio():
#     return "<h1>Hola mundo con Flask</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)