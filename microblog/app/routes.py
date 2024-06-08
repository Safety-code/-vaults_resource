from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in portland'},
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was cool'}
    ]

    return render_template('index.html', title='Home', user=user, posts=posts, )
