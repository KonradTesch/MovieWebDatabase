from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

engine = create_engine("sqlite:///db.sql")

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    director = db.Column(db.String(100))
    poster_url = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)