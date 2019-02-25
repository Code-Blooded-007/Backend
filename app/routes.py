from flask import render_template
from app import app



@app.route('/')
@app.route('/index')
def index():
	websites = [
		{'name' : 'google.com', 'status' :'active'},
		{'name' : 'ghrcem.net', 'status' : 'not active'}
	]
	return render_template('index.html', title='Home', websites=websites)
