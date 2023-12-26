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

@bp.route('/app01')
@login_required
def app01():
    #return 'dashboard'
     return render_template('dashboard/dash.html' , dash_url='/wij_dashapp1')

@bp.route('/app02')
def app02():
    return render_template('dashboard/dash.html' , dash_url= '/wij_dashapp2' )

@bp.route('/app03')
def app03():
    return render_template('dashboard/dash.html' , dash_url= '/wij_dashapp3' )