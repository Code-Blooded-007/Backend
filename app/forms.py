from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError
from app.models import Admin


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	name = StringField('Full Name', validators = [DataRequired()])
	email = StringField('Email', validators = [DataRequired(), Email()])
	phone_number = StringField('Phone Number', validators = [DataRequired()])
	password = PasswordField('password', validators = [DataRequired(), Length(min=8, max=32)])
	confirm_password =  PasswordField('Confirm password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = Admin.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('email address already in use.')

	def validate_phone_number(self, phone_number):
		user = Admin.query.filter_by(phone_number=phone_number.data).first()
		if user is not None:
			raise ValidationError('phone number already in use.')

