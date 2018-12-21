"""app.routes
This module contains all of the routes for the app.
"""
from app import app
from models.league import League
from flask import jsonify, render_template


@app.route('/')
@app.route('/index')
def index():
    """
    Home page end point. If no league exists, the first hit will allow the
    user to set up defaults for the league. These can be changed later.
    This will otherwise show the front page of the site

    Returns:
        Flask.Response: Response for page
    """
    if(League.query.first()):
        league = league.query.first()
        return jsonify({'League':{'name':league.name, 'tagline':league.tagline}})
    else:
        return render_template('create_league.html')