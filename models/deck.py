"""models.deck

This module contains the Deck Model
"""
from app import db
from sqlalchemy import sql


class Deck(db.Model):
    __tablename__ = 'deck'
    """
    This model contains information about a deck. Decks are owned by a single
    player unless traded. Decks have seasonal instances to track performance
    by season. 