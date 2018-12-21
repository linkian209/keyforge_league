"""keyforge_league.py

A simple flask app that runs a Keyforge League.
"""
from app import app
from app import db
from app import routes #noqa
from flask_migrate import Migrate
from models.user import User #noqa
from models.league import League #noqa


db.app = app
db.init_app(app)
migrate = Migrate(app, db)