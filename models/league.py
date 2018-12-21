"""models.league

This module contains the League Model
"""
from app import db
from sqlalchemy import sql


class League(db.Model):
    __tablename__ = 'league'
    """
    This model contains information about the league.

    Attributes:
        name (str): League Name
        tagline (str): League Tagline
    """
    # Attributes
    name = db.Column(db.String(128), primary_key=True)
    tagline = db.Column(db.String(256), nullable=False)

    # Functions
    def __repr__(self):
        """
        This returns the string representation of the League

        Returns:
            str: The string representaion
        """
        return '<League {}>'.format(self.name)