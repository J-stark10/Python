from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shooll.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Denicion del modelo n - m escenario (B)
# Tabla intermedia
student_course = db.Table(
    'student_course',
    db.Column("student_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True)
)

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    courses = db.relationship('Course',secondary=student_course,back_populates='students')

    def __repr__(self):
        return f"Estudiante: nombre={self.name}"

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)

    students = db.relationship('Student',secondary=student_course,back_populates='courses')

    def __repr__(self):
        return f"Curso: titulo: {self.title}"

# Inicializar la base de datos    
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de Datos Inicializada correctamente")

# Insertar registros
def insert_data():
    with app.app_context():
        # Crear estudiantes
        s1 = Student(name="Javier Jose")
        s2 = Student(name="Yack Michael")
        s3 = Student(name="Rudy Cristhian")

        # Crear cursos
        c1 = Course(title="NodeJS")
        c2 = Course(title="React")
        c3 = Course(title="Programacion con JS")

        s1.courses.extend([c1,c2]) # Registro de Javier a Fullstack y JS
        s2.courses.append(c2) #append (uno solo) y extend(mas de uno)
        s3.courses.extend([c1,c3])

        db.session.add_all([s1,s2,s3,c1,c2,c3])
        db.session.commit()
        print("Estudiantes y Cursos insertados correctamente")

def query_data():
    with app.app_context():
        print("\nListado de estudiantes y sus cursos")
        students = Student.query.all()
        for student in students:
            print(f"\n{student.name} esta inscrito en: ")
            for course in student.courses:
                print(f"- {course.title}")
        
        print('\nListado de cursos y sus estudiantes')
        courses = Course.query.all()
        for course in courses:
            print(f"\n{course.title} tiene inscritos a: ")
            for student in course.students:
                print(f"- {student.name}")

def update_data():
    with app.app_context():
        print('\n Agregando un curso a un estudiante')

        student = Student.query.filter_by(id=1).first()
        course = Course.query.filter_by(id=2).first()

        if student and course:
            student.courses.append(course)
            db.session.commit()
            print('\n Inscripcion actualizada')
        else:
            print("Estudiante o curso no encontrado")

def delete_data():
    with app.app_context():
        print("\nEliminación de la inscripcion en un curso")
        student = Student.query.filter_by(id=1).first()
        course = Course.query.filter_by(id=3).first()

        if student and course:
            student.courses.remove(course)
            db.session.commit()
            print("\nInscripción eliminada")
        else:
            print('\nEstudiante o curso no encontrado')


if __name__ == "__main__":
    #init_db()
    #insert_data()
    #query_data()
    #update_data()
    delete_data()
    query_data()