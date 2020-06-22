from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
@app.route('/about')
def index():
    return render_template('index.html', title='Home Page')

def about():
    return  render_template('about.html', title='About Us')
