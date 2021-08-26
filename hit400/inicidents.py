from flask_restful import Resource, reqparse
from models import Incidents
from datetime import datetime

class IncidentRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('number',
        type=str,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument('audio',
        type=str,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument('lattitude',
        type=str,
        required=True,
        help="This field cannot be left blank")
    parser.add_argument('longitude',
        type=str,
        required=True,
        help="this field cannot be left blank")


    def post(self):
        data = IncidentRegister.parser.parse_args()

        incidents = Incidents(phone_number=data['number'], audio=data['audio'], lattitude=data['lattitude'], 
                            longitude=data['longitude'], reported_on=datetime.now())
        incidents.save_to_db()

        return {'message': 'request posted succesfully'}, 201