from flask_wtf import Form
from wtforms import SelectField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class LoginForm(Form):
    username = StringField('User Name', validators = [InputRequired("Please enter a username")])
    password = PasswordField('Password', validators = [InputRequired("Please enter a password")])
    submit =  SubmitField('Login')

class RegisterForm(Form):
    email = StringField('Email', validators = [InputRequired("Please enter a email")])
    password = PasswordField('Password', validators = [InputRequired("Please enter a password")])
    submit =  SubmitField('Register')
