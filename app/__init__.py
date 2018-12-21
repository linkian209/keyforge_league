"""app

This module contains the reference to the app and the database.

Attributes:
    app (Flask): The Flask Application
    db (SQLAlchemy): The database
"""
import sys

from app import funcs
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

login_manager = LoginManager(app)

# Get config based on Flask environment
if(app.config['ENV'] == 'development'):
    app.config.from_object('app.config.DevelopmentConfig')
elif(app.config['ENV'] == 'testing'):
    app.config.from_object('app.config.TestingConfig')
else:
    # Production config. Make sure environment variables exist
    if(funcs.mysqlEnvSet()):
        app.config.from_object('app.config.ProductionConfig')
    else:
        print(' ! Missing MySQL Environment Config! Exiting...')
        sys.exit()

# Check if the secret key is set
if(funcs.secretKeySet()):
    app.secret_key = funcs.getSecretKey()
else:
    print(' ! Missing Secret Key! Exiting...')
    sys.exit()

db = SQLAlchemy()