import os
from os.path import join, dirname, realpath

basedir = os.path.abspath(os.path.dirname(__file__))


#SQLALCHEMY DATABASE CONFIGURATIONS
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'HIT400.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#FLASK-WTF CONIGURATIONS
WTF_CSRF_ENABLED = True 
SECRET_KEY = 'catering-for-everyone-by-nathan'

#FLASK-BASIC-AUTH CONFIGURATIONS
BASIC_AUTH_USERNAME = 'Admin'
BASIC_AUTH_PASSWORD = 'cateringAdmin'

#Uploads 
UPLOAD_FOLDER_LOGO = join(dirname(realpath(__file__)), 'static/images/logos/')
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/assets/images/uploads/')

#FLASK_LOGIN