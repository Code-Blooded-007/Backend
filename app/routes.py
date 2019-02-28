from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm


@app.route('/')
@app.route('/index/')
@app.route('/home/')
def index():
	websites = [
		{'name' : 'google.com', 'status' :'active'},
		{'name' : 'ghrcem.net', 'status' : 'active'},
		{'name' : 'mis.com', 'status' : 'not active'},
		{'name' : 'github.com', 'status' : 'active'},
		{'name' : 'w3school.com', 'status' : 'active'}
	]
	return render_template('index.html', title='Home', websites=websites)


@app.route('/login/', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "test@test.com" and form.password.data == "password":
			flash('You have been logged in', 'success')
			return redirect(url_for('index'))
		else:
			flash('Login unsuccessful!', 'danger')
	return render_template('login.html', title="Login", form=form)


@app.route("/register/", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for { form.name.data }!', 'success')
		return redirect(url_for('index'))
	return render_template('register.html', title="Register", form=form)
