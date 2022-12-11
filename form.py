from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from wtforms import StringField, SubmitField, PasswordField, BooleanField



class LoginForm(FlaskForm):
    username =  StringField('Username', validators=[DataRequired(), 
                            Length(min=2, max=20), Regexp('^[a-zA-Z0-9_\d-]+$', message='Only alphabets, numbers, dash and underscore allowed')])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20), Regexp('^[a-zA-Z0-9!@#$&*]+$', message='Enter alphabets, numbers and special characters(!@#$&*) only')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class LoginForm1(FlaskForm):
    username =  StringField('Username', validators=[DataRequired(), 
                            Length(min=2, max=20), Regexp('^[a-zA-Z0-9_\d-]+$', message='Only alphabets, numbers, dash and underscore allowed')])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20), Regexp('^[a-zA-Z0-9!@#$&*]+$', message='Enter alphabets, numbers and special characters(!@#$&*) only')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')