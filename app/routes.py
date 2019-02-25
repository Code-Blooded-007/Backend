from flask import render_template
from app import app



@app.route('/')
@app.route('/index')
def index():
	websites = {
		'google.com' : 'active',
		'ghrcem.net' : 'not active'
	}
    return render_template('index.html', title='Home', websites=websites)
