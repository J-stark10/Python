from flask import request, render_template, url_for, redirect, Blueprint

from src.app import db

bp_core  = Blueprint('core', __name__, template_folder='templates')

@bp_core.route('/')
def index():
    return render_template('core/index.html')