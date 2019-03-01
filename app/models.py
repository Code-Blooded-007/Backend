from app import db

class Admin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200))
	email = db.Column(db.String(120), unique=True, nullable=False, index=True)
	phone_number = db.Column(db.String(20), unique=True, nullable=False, index=True)
	password_hash = db.Column(db.String(128), nullable=False)
	websites = db.relationship('Website', backref='admin', lazy='dynamic')

	def __repr__(self):
		return f'<User {self.name}>'

class Website(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	url = db.Column(db.String(100), unique=True, nullable=False, index=True)
	http_status_code = db.Column(db.Integer, default=200)
	message_sent = db.Column(db.Boolean, default=False)
	remark = db.Column(db.String(200), default='N/A', nullable=False)
	approved = db.Column(db.Boolean, default=False)
	admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

	def __repr__(self):
		return f'<Website {self.name}>'