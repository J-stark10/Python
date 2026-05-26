from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_equipo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # importacion de bp
    from src.core.routes import bp_core
    from src.miembros.routes import bp_miembro
    from src.tareas.routes import bp_tarea

    # resgistrar el bp
    app.register_blueprint(bp_core, url_prefix='/')
    app.register_blueprint(bp_miembro, url_prefix='/miembros')
    app.register_blueprint(bp_tarea, url_prefix='/tareas')

    return app