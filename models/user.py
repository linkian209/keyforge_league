"""models.user

This Module contains the User Model
"""
from app import db
from flask_login import UserMixin
from sqlalchemy import sql


class User(UserMixin, db.Model):
    ___tablename__ = 'user'
    """
    This model is used to store users. There is a mixin that manages sessions as well.

    Attributes:
        id (int): User ID
        name (str): User's Name
        email (str): User's Email
        password (str): A hashed version of the User's password
        decks (relationship): Decks owned by user
        seasons (relationship): Player's seasonal instances
        total_wins (int): Total number of agmes this user has won
        total_losses (int): Total number
        create_date (DateTime): When the user was created
        update_date (DateTime): When the user was last updated

    Args:
        :param UserMixin: The Mixin from flask_login that maintains sessions
        :param db.Model: SQLAlchemy base class
    """
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    decks = db.relationship(
        'Deck', backref='user', lazy=True, passive_deletes=True
    )
    seasons = db.relationship('SeasonPlayer', backref='user')
    total_wins = db.Column(db.Integer, default=0)
    total_losses = db.Column(db.Integer, default=0)
    create_date = db.Column(db.DateTime, server_default=sql.func.now())
    update_date = db.Column(
        db.DateTime, server_default=sql.func.now(), onupdate=sql.func.now()
    )

    # Functions
    def __repr__(self):
        """
        Representaion of this object as a string

        Args:
            :param self: This user object

        Returns:
            str: String representation of the user
        """
        return '<User {}>'.format(self.name)