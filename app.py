from flask import Flask
from models import db, User, Movie

app = Flask(__name__)

def setup_database():
    with app.app_context():
        db.create_all()