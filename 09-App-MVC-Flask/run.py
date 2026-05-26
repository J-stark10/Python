from flask import Flask, request
from database import db #importamos instacia

from controllers import user_controller,client_controller,product_controller,sale_controller

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ventas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(user_controller.user_bp)
app.register_blueprint(client_controller.client_bp)
app.register_blueprint(product_controller.product_bp)
app.register_blueprint(sale_controller.sale_bp)

@app.context_processor
def inject_active_path():
    def is_active(path):
        if request.path == path:
            return 'bg-zinc-800 text-white font-semibold'
        return 'text-zinc-400 hover:bg-zinc-800 hover:text-white'
    return(dict(is_active = is_active))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)