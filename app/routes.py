from flask import render_template
from app import app



@app.route('/')
@app.route('/index')
def index():
	websites = [
		{'name' : 'google.com', 'status' :'active'},
		{'name' : 'ghrcem.net', 'status' : 'active'},
		{'name' : 'mis.com', 'status' : 'not active'},
		{'name' : 'github.com', 'status' : 'active'},
		{'name' : 'w3school.com', 'status' : 'active'}
	]
	return render_template('index.html', title='Home', websites=websites)