from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), length(min=2, max=30)])
    password = PasswordField('Password', validators=[InputRequired(), length(min=2, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(),
                                                                     EqualTo('password')])
    email = EmailField('Email', validators=[InputRequired(), Email()])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), length(min=2, max=30)])
    password = PasswordField('Password', validators=[InputRequired(), length(min=2, max=30)])


class ForgotPasswordForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), length(min=2, max=30)])
    email = EmailField('Email', validators=[InputRequired(), Email()])


class NewPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired(), length(min=2, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
