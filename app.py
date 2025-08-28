from flask import Flask
import os
from models import db, User, Movie
from data_manager import DataManager

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, 'data/movies.db')}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

data_manager = DataManager()


@app.route('/')
def home():
    return "Welcome to MoviWeb App!"

@app.route('/users')
def list_users():
    users = data_manager.get_users()
    return str(users)  # Temporarily returning users as a string

@app.route('/users', methods=['POST'])
def add_user():
    pass

@app.route('/users/<int:user_id>/movies', methods=['GET', 'POST'])
def handle_user_movies(user_id):
    pass


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_user_movie(user_id, movie_id):
    pass


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_user_movie(user_id, movie_id):
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run()