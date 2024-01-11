from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('main/index.html')


#@bp.route('/')
#def index():
#    return redirect(url_for('question._list'))
