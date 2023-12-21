from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Numeric(10))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    games = db.relationship('Game')