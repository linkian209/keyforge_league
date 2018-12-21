"""models.game

This module contains the Game Model
"""
from app import db
from sqlalchemy import sql


class Game(db.Model):
    __tablename__ = 'game'
    """
    This model contains the information for an individual game part of a match.
    
    Attributes:
        id (int): The unique ID of the game
        match_id (int): The ID of the match this game is a part of
        player_1_id (int): ID of the player that went first
        deck_1_id (int): ID of the deck that went first
        player_2_id (int): ID of the player that went second
        deck_2_id (int): ID of the deck that went second
        create_date (DateTime): Time the game was entered
        winner (int): ID of the winning player
    """
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(
        db.Integer, db.ForeignKey('match.id', ondelete='CASCADE')
    )
    player_1_id = db.Column(db.Integer, nullable=False)
    deck_1_id = db.Column(db.Integer, nullable=False)
    player_2_id = db.Column(db.Integer, nullable=False)
    deck_2_id = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, server_default=sql.func.now())
    winner = db.Column(db.Integer)

    # Functions
    def __repr(self):
        """
        Returns the string representation of the object

        Args:
            :param self: The object

        Returns:
            str: The string representation
        """
        return '<Game {} - {} v. {}>'.format(
            self.id, self.player_1_id, self.player_2_id
        )