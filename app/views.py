from app import app

from app.forms import LoginForm
from app.models import User
from flask import render_template, redirect, url_for
from flask_login import current_user, login_user


@app.route('/')
def home():
    app.logger.debug('Hello, World!')
    return 'Hello, World!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)