from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

from index import db
from index.forms import AnswerForm
from index.models import Question, Answer
from index.views.auth_views import login_required

import dash
from dash import Dash , dcc , html
from index.views.auth_views import login_required

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/app/<appid>')
@login_required
def app(appid):
     return render_template('dashboard/dash.html' , dash_url=('/'+appid))

