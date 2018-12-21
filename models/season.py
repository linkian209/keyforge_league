"""models.season

This module contains the Season Module
"""
from app import db
from sqlalchemy import sql


class Season(db.Model):
    __tablename__ = 'season'
    """
    This model contains the data for each season. Seasons have a specific
    duration. Seasons are comprised of players, decks, and matches. The Season
    model will track matches between players and their decks and at the end
    calculate statistics for the season.

    Attributes:
        id (int): Unique Season ID
        start_date (DateTime): Starting date of the Season
        end_date (DateTime): Ending date of the Season
        matches (relationship): All matches that take place in the season
        players (relationship): All players that are in the season
        decks (relationship): All decks that were played in the season
    """
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, server_default=sql.func.now())
    end_date = db.Column(db.DateTime)
    matches = db.relationship(
        'Match', backref='season', lazy=True, passive_deletes=True
    )
    players = db.relationship(
        'SeasonPlayer', backref='season', lazy=True, passive_deletes=True
    )
    players = db.relationship(
        'SeasonDeck', backref='season', lazy=True, passive_deletes=True
    )
    
    # Functions
    def __repr__(self):
        """
        Returns string representation of the season

        Args:
            :param self: This season

        Returns:
            str: The string representation
        """
        return '<Season {}>'.format(self.id)