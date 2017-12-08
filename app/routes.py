from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'karthikrk1'}
    posts = [
        {
            'author': {'username': 'Kaushik'},
            'body': 'Beautiful day in Hamburg!'
        },
        {
            'author': {'username': 'Vignesh'},
            'body': 'The food was great!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)
