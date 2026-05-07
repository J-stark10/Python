#Relaciones 1 - N con ORM
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Declaracion para usar SQLAlchemy
db = SQLAlchemy(app)

#Crear los modelos
class User(db.Model):
    __tablename__ = "users"
    

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)

    #Crear un campo virtual para la relacion posts y registro en cascada (si se borra un usuario, se borran sus posts)
    posts = db.relationship("Post", back_populates = "user", cascade = "all, delete-orphan")

    def __repr__(self):
        return f"<Usuario: name: {self.name}, email: {self.email}>"

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    #User id LLave foranea 
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    
    #Crear un campo virtual para la relacion con users
    user = db.relationship("User", back_populates = "posts")
    
    def __repr__(self):
        return f"<POST: title: {self.title} user: {self.user.name} -> {self.user.email}>"

# funcion para inicializar la base de datos
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos inicializada.")

# Operaciones CRUD
# Insertar productos (manual)
def insert_data():
    with app.app_context():
        # Crear objetos de tipo usuario
        user1 = User(name="Javier Jose",email="javier.jose@example.com")
        user2 = User(name="María García",email="maria.garcia@example.com")
        user3 = User(name="Carlos López",email="carlos.lopez@example.com")

        # Crear objetos para entradas
        post1 = Post(title="Primer Post", content="Contenido del primer post", user=user1)
        post2 = Post(title="Segundo Post", content="Contenido del segundo post", user=user1)
        post3 = Post(title="Tercer Post", content="Contenido del tercer post", user=user2)
        post4 = Post(title="Cuarto Post", content="Contenido del cuarto post",user=user3)

        # Adición de objetos (registros en la tabla)
        db.session.add_all([user1, user2, user3, post1, post2, post3, post4])

        # Consolida los cambios en la base de datos
        db.session.commit()
        print("Usuarios insertados exitosamente.")

# Consulta de datos
def query_data():
    with app.app_context():
        print("\nListado de usuarios y sus publicaciones:")

        #Obtener todos los registros
        users = User.query.all()
        for user in users:
            print(f"\n {user}")
            for post in user.posts:
                print(post)

def update_data(): 
    # Actualizar post
    with app.app_context():
        print("\nActualizando una publicación...")
        post  = Post.query.filter_by(id=3).first()
        if post: 
            post.content = "Contenido actualizado del tercer post"
            db.session.commit()
            print("Publicación actualizada exitosamente.")
            query_data()
        else:
            print("Publicación no encontrada.")

def delete_data():
    # Eliminar un usuario y sus publicaciones en cascada
    with app.app_context():
        print("\nEliminando un usuario y sus publicaciones...")
        user = User.query.filter_by(id=1).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            print("Usuario eliminado exitosamente.")
            query_data()
        else:
            print("Usuario no encontrado.")

if __name__ == "__main__":
    init_db()
    insert_data()
    query_data()    
    update_data()
    delete_data()