from flask import render_template, redirect, url_for, flash, jsonify, make_response, request
from flask_login import login_user, logout_user, current_user
from . import app, db, lm, api
from .forms import LoginForm, RegisterForm, ResponseTeamForm, PatientForm
from .models import User, Response_Team, Hospitals, Incidents, Patient
from datetime import datetime
from flask_jwt import JWT
from werkzeug.utils import secure_filename
import os
from inicidents import IncidentRegister
from patientAuth import PatientAuth
from twilio.rest import Client

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

api.add_resource(IncidentRegister, '/incidents')
api.add_resource(PatientAuth, '/PatientAuth')


@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('login Successful')
            return redirect(url_for('index'))
    return render_template('login.html', form=form)
    
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/blank')
def blank():
    return render_template('blank.html')

@app.route('/getdirections')
def GetDirections():
    return render_template('getdirections.html')

@app.route('/hospitals', methods=['GET','POST'])
def hospitals():
    return render_template('hospitals.html', hospitals = Hospitals.query.all())

@app.route('/mapview')
def mapview():
    return render_template('mapview.html', )

@app.route('/test')
def test():
    return render_template('testmaps.html', )

@app.route('/Patientnotification')
def Patientnotification():
    account_sid = "AC508537ec02af8aa37a56dd2da6be2ec6"
    print "hello there"
    auth_token  = "8d2bac0979bec856a4d635cf07282c49"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    to="+263774428916", 
    from_="+14057035412",
    body="We have recieved an incident alert from your next of keen!, We glad to tell you that we working on it")
    print(message.sid)
    return render_template('patientNotification.html', patients = Patient.query.all(), incidents = Incidents.query.all())

@app.route('/patients')
def patients():
    return render_template('patients.html', patients = Patient.query.all())

@app.route('/newpatient', methods=['GET','POST'])
def newpatient():
    form = PatientForm()
    if form.validate_on_submit():
        f = form.image.data
        pic = secure_filename(f.filename)

        patient = Patient(name=form.name.data, surname=form.surname.data, national_id=form.national_id.data, gender=form.gender.data, BirthDate=form.BirthDate.data,
                phone_numbers=form.phone_number.data, phone_numbers2=form.phone_number2.data, email=form.email.data, image=pic,
                marital=form.marital.data, age=form.age.data, race=form.race.data, patient_history=form.patient_history.data,
                nextOfKeen=form.nextOfKeen.data, NOKsurname=form.NOKsurname.data, relationship=form.relationship.data, street=form.street.data,
                surburb=form.surburb.data, city=form.city.data, registered_on=datetime.now(), password_hash=form.password.data)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], pic))
        db.session.add(patient)
        db.session.commit()
        flash('Registration succesful')
        return redirect(url_for('newpatient'))
    return render_template('add_patient.html',form=form)

@app.route('/newadministrator', methods=['GET','POST'])
def newadministrator():
    form = RegisterForm()
    if form.validate_on_submit():
        new = User(name=form.name.data, surname=form.surname.data,employee_id=form.employee_id.data, username=form.username.data,
                    email=form.email.data, password_hash=form.password.data, registered_on=datetime.now())
        db.session.add(new)
        db.session.commit()
        flash('Registration succesful')
        return redirect(url_for('newadministrator'))
    return render_template('add_administrator.html', form=form, users = User.query.all())

@app.route('/newresponseteam', methods=['GET','POST'])
def newresponseteam():
    form = ResponseTeamForm()
    if form.validate_on_submit():
        new = Response_Team(name=form.name.data, surname=form.surname.data,employee_id=form.employee_id.data,
                    email=form.email.data,phone_number=form.phone_number.data, registered_on=datetime.now())
        db.session.add(new)
        db.session.commit()
        flash('Registration succesful')
        return redirect(url_for('newresponseteam'))
    return render_template('add_responseteam.html', form=form, response_team = Response_Team.query.all())

@app.route('/ViewIncidents')
def ViewIncidents():
    return render_template('viewIncidents.html', Incidents= Incidents.query.all())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500