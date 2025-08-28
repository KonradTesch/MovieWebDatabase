from flask import Flask, render_template, request, redirect, url_for
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
    users = data_manager.get_users()
    return render_template("index.html", users=users)


@app.route('/users', methods=['POST'])
def add_user():
    name = request.form.get('name')

    data_manager.create_user(name)
    return redirect(url_for('home'))

@app.route('/users/<int:user_id>/movies', methods=['GET', 'POST'])
def handle_user_movies(user_id):
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')

        data_manager.add_movie(user_id, title, year)
        return redirect(url_for('handle_user_movies', user_id=user_id))
    #get request
    movies = data_manager.get_user_movies(user_id)

    return render_template(movies.html, movies=movies)


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_user_movie(user_id, movie_id):
    pass


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_user_movie(user_id, movie_id):
    data_manager.delete_user_movie(user_id, movie_id)
    return redirect(url_for('handle_user_movies', user_id=user_id))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run()