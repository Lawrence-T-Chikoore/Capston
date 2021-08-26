"""
The flask application package.
"""
import sys
import logging
from os.path import join,dirname, realpath

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_restful import  Api
#from flask_basicauth import BasicAuth
from flask_moment import Moment

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/assets/images/uploads')

lm = LoginManager()

app = Flask(__name__)
app.logger.setLevel(logging.ERROR)
app.config.from_object('config')
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
lm.init_app(app)
lm.session_protection = "strong"
lm.login_view = "login"
#basic_auth = BasicAuth(app)
moment = Moment(app)
api = Api(app)

from views import *
