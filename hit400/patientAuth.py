from flask_restful import Resource, reqparse
from models import Patient
from datetime import datetime
from flask_login import login_user, logout_user, current_user

class PatientAuth(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('number',
        type=str,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank")


    def post(self):
        data = PatientAuth.parser.parse_args()


        user = Patient.query.filter_by(phone_numbers = data['number']).first()
        if user is not None and user.check_password(password = data['password']):
            login_user(user)
            return {'message': 'login successful'}, 201
        return {'message': 'Incorrect Username or Password'}