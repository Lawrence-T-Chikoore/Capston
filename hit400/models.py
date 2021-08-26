from datetime import datetime, date
from hashlib import md5

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from hit400 import db 


class Patient(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    national_id = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    phone_numbers = db.Column(db.String(80), unique=True)
    phone_numbers2 = db.Column(db.String(80))
    registered_on = db.Column(db.DateTime, nullable=False)
    marital_status = db.Column(db.String(100))
    race = db.Column(db.String(100))
    BirthDate = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    netxOfKeen = db.Column(db.String(100))
    NOKsurname = db.Column(db.String(100))
    relationship = db.Column(db.String(100))
    patient_history = db.Column(db.String(500))
    age = db.Column(db.Integer)
    street = db.Column(db.String(80))
    location = db.Column(db.String(80))
    surburb = db.Column(db.String(80))
    city = db.Column(db.String(80))
    profile_picture = db.Column(db.String(80))
    password_hash = db.Column(db.Text)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    def __init__(self, name, surname, national_id, gender, BirthDate, phone_numbers, phone_numbers2, email, image, marital, age, race,  patient_history, nextOfKeen, NOKsurname, relationship, street, surburb, city, registered_on, password_hash):
        self.name = name
        self.surname = surname
        self.national_id = national_id
        self.gender =gender
        self.BirthDate =BirthDate
        self.phone_numbers= phone_numbers
        self.phone_numbers2= phone_numbers2
        self.email= email
        self.profile_picture=image
        self.marital_status= marital
        self.age= age
        self.race= race
        self.patient_history=patient_history
        self.netxOfKeen=nextOfKeen
        self.NOKsurname= NOKsurname
        self.relationship= relationship
        self.street= street
        self.surburb=surburb
        self.city= city
        self.registered_on=registered_on
        self.set_password(password_hash)
        self.confirmed = False

    def __repr__(self):
        return "patient {}".format(self.name)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    username = db.Column(db.String(100))
    employee_id = db.Column(db.String(100))
    email = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(80))
    last_seen = db.Column(db.DateTime)
    registered_on = db.Column(db.DateTime, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    def __init__(self, name,surname,employee_id, username, email, password_hash, registered_on):
        self.name = name
        self.surname = surname
        self.employee_id = employee_id
        self.username = username
        self.email = email
        self.registered_on = registered_on
        self.set_password(password_hash)
        self.confirmed = False

    def __repr__(self):
        return "user {}".format(self.name)

class Response_Team(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    employee_id = db.Column(db.String(100))
    email = db.Column(db.String(80), unique=True)
    phone_number = db.Column(db.String(80), unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    def __init__(self, name,surname,employee_id, email, registered_on, phone_number):
        self.name = name
        self.surname = surname
        self.employee_id = employee_id
        self.email = email
        self.registered_on = registered_on
        self.phone_number = phone_number
    
    def __repr__(self):
            return "member {}".format(self.name)

class Hospitals(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Hospital = db.Column(db.String(80), nullable=False)
    lattitude = db.Column(db.String(80), unique=True, nullable=False)
    longitude = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, Hospital, lattitude, longitude):
        self.Hospital = Hospital
        self.lattitude = lattitude
        self.longitude = longitude

    def __repr__(self):
        return self.name

class Incidents(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(80), nullable=False)
    audio = db.Column(db.Text, nullable=False)
    lattitude = db.Column(db.String(80), unique=True, nullable=False)
    longitude = db.Column(db.String(80), unique=True, nullable=False)
    reported_on = db.Column(db.DateTime)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, phone_number, lattitude, longitude, audio, reported_on):
        self.phone_number = phone_number
        self.audio = audio
        self.lattitude = lattitude
        self.longitude = longitude
        self.reported_on = reported_on

    def __repr__(self):
        return self.name