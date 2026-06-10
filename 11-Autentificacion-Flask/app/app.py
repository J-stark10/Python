from flask import Flask
from flask_migrate import Migrate
from app.extensions import db, bcrypt, login_manager
from app.models import User

migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder="templates")

    app.config.from_object("app.config.Config")
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    migrate.init_app(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Importacion de el Blueprint
    from app.main import main_bp
    from app.auth import auth_bp

    # Registro de el Blueprint
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app