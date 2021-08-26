from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """ A simple login form """
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    
class RegisterForm(FlaskForm):
    """ A simple Registration Form """
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    employee_id = StringField('employee_id', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('confirm password')

class ResponseTeamForm(FlaskForm):
    """ A simple Response Team registration Form """
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    employee_id = StringField('employee_id', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    phone_number = StringField('phone_number', validators=[DataRequired()])

class PatientForm(FlaskForm):
    """ A simple Patient Registration Form """
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    national_id = StringField('surname', validators=[DataRequired()])
    marital = StringField('marital_status', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    phone_number = StringField('phone_number', validators=[DataRequired()])
    phone_number2 = StringField('phone_number', validators=[DataRequired()])
    race = StringField('race', validators=[DataRequired()])
    gender = StringField('gender', validators=[DataRequired()])
    nextOfKeen = StringField('netxOfKeen', validators=[DataRequired()])
    NOKsurname = StringField('netxOfKeen', validators=[DataRequired()])
    relationship = StringField('relationship', validators=[DataRequired()])
    patient_history = StringField('patient_history', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    street = StringField('street', validators=[DataRequired()])
    BirthDate = StringField('location', validators=[DataRequired()])
    surburb = StringField('surburb', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    image = StringField('profile_picture', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('confirm password')
