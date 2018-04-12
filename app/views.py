from app import app, db

from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask import render_template, redirect, url_for, flash, abort
from flask_login import current_user, login_user, logout_user


@app.route('/setup/', methods=['GET', 'POST'])
def setup():
    users = User.query.all()
    if users:
        abort(404)
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data != form.password_confirm.data:
            flash('Passwords do not match')
            return redirect(url_for('setup'))
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('setup.html', form=form)

@app.route('/')
def index():
    app.logger.debug('Hello, World!')
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))