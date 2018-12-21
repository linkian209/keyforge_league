"""models.match

This module contains the Match Model
"""
from app import db
from models import Game
from sqlalchemy import sql



class Match(db.Model):
    __tablename__ = 'match'
    """
    This model contains data about a specific match between specific players
    and specific decks. Each match contains some number of games. The winner
    of the match is the one with the most wins.

    Attributes:
        id (int): Unique ID of the match
        season (Foreign Key): The season of the match
        player_1_id (Foreign Key): The ID of player 1 in the match
        player_1 (relationship): The relation between player object and match
        deck_1_id (Foreign Key): The ID of player ones's deck for the match
        deck_1 (relationship): The relation between deck object and the match
        player_2_id (Foreign Key): The second player in the match
        player_2 (relationship): The relation between player object and match
        deck_2_id (Foreign Key): The second player's deck for the match
        deck_2 (relationship): The relation between deck object and the match
        create_date (DateTime): The date the match was created
        update_date (DateTime): The date the match was last updated
        games (relationship): Individual games that took place as a part
                              of this match
        winning_player (int): ID of the winning player of the match
        winning_deck (int): ID of the winning deck of the match
        winner_games (int): Number of games won by the winner
        losing_player (int): ID of the losing player of the match
        losing_deck (int): ID of the losing deck of the match
        loser_games (int): Number of games won by the loser
    """
    # Attributes of the match
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(
        db.Integer, db.ForeignKey('season.id'), nullable=False
    )
    player_1_id = db.Column(
        db.Integer, db.ForeignKey('player.id'), nullable=False
    )
    player_1 = db.relationship(
        'SeasonPlayer', foreign_keys=[player_1_id], backref='player_1_matches'
    )
    deck_1_id = db.Column(
        db.Integer, db.ForeignKey('deck.id'), nullable=False
    )
    deck_1 = db.relationship(
        'SeasonDeck', foreign_keys=[deck_1_id], backref='deck_1_matches'
    )
    player_2_id = db.Column(
        db.Integer, db.ForeignKey('player.id')
    )
    player_2 = db.relationship(
        'SeasonPlayer', foreign_keys=[player_2_id], backref='player_2_matches'
    )
    deck_2_id = db.Column(
        db.Integer, db.ForeignKey('deck.id'), nullable=False
    )
    deck_2 = db.relationship(
        'SeasonDeck', foreign_keys=[deck_2_id], backref='deck_2_matches'
    )
    create_date = db.Column(db.DateTime, server_default=sql.func.now())
    update_date = db.Column(
        db.DateTime, server_default=sql.func.now(), onupdate=sql.func.now()
    )
    games = db.relationship('Game')
    # Results varaiables
    winning_player = db.Column(db.Integer)
    winning_deck = db.Column(db.Integer)
    winning_games = db.Column(db.Integer)
    losing_player = db.Column(db.Integer)
    losing_deck = db.Column(db.Integer)
    losing_games = db.Column(db.Integer)

    # Functions
    def __repr__(self):
        """
        Returns string representation of a match

        Args:
            :param self: This object

        Returns:
            str: The string representation
        """
        return '<Match {} - {} v. {}>'.format(
            self.id, self.player_1_id, self.player_2_id
        )

    def endMatch(self):
        """
        Ends the match. This will determine the winner and populate the results
        into the results varaibles. This will return a dictionary with the 
        following format:
            {
                'winner': {
                    'player': [player ID],
                    'deck': [Deck ID],
                    'games': [Games won]
                },
                'loser': {
                    'player': [player ID],
                    'deck': [Deck ID],
                    'games': [Games won]
                }
            }

        Args:
            :param self: This object

        Returns:
            dict: A dictionary containing the results of the match
        """
        retval = {'winner':{}, 'loser':{}}
        player_1 = {
            'player': self.player_1_id, 'deck': self.deck_1_id, 'games':0
        }
        player_2 = {
            'player': self.player_2_id, 'deck': self.deck_2_id, 'games':0
        }

        # Loop through games
        for game in self.games.all():
            if(game.winner is self.player_1_id):
                player_1['games'] += 1
            else:
                player_2['games'] += 1

        # Results!
        if(player_1['games'] >= player_2['games']):
            self.winning_deck = self.deck_1_id
            self.winning_player = self.player_1_id
            self.winning_games = player_1['games']
            self.losing_deck = self.deck_2_id
            self.losing_player = self.player_2_id
            self.losing_games = player_2['games']
            retval['winner'] = player_1
            retval['loser'] = player_2
        else:
            self.winning_deck = self.deck_2_id
            self.winning_player = self.player_2_id
            self.winning_games = player_2['games']
            self.losing_deck = self.deck_1_id
            self.losing_player = self.player_1_id
            self.losing_games = player_1['games']
            retval['winner'] = player_2
            retval['loser'] = player_1

        # Update DB
        db.session.commit()

        return retval