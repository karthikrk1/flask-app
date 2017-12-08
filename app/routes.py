from flask import render_template
from app import app

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
