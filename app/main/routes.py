from flask import g, render_template, current_app, redirect, url_for, flash, request,jsonify
from app.main.forms import SearchForm
from app.main import bp

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home Page')

@bp.route('/about')
def about():
    return  render_template('about.html', title='About Us')
