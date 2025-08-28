from flask import Flask, render_template, request, redirect, url_for
import os
from models import db, User, Movie
from data_manager import DataManager, APIError

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, 'data/movies.db')}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

data_manager = DataManager()


@app.route('/')
def home():
    """
    Displays the home page with a list of all users.
    :return: Rendered HTML page with user list
    """
    users = data_manager.get_users()
    return render_template("index.html", users=users)


@app.route('/users', methods=['POST'])
def add_user():
    """
    Adds a new user to the database based on form data.
    :return: Redirect to home page
    """
    try:
        name = request.form.get('name')
        if not name:
            raise ValueError('Name is required')
        data_manager.create_user(name)
    except ValueError as e:
        print(f"Value Error: {e}")
    return redirect(url_for('home'))


@app.route('/users/<int:user_id>/movies', methods=['GET', 'POST'])
def handle_user_movies(user_id):
    """
    Handles GET and POST requests for user movies.
    GET: Displays all movies for a specific user.
    POST: Adds a new movie to a user's collection.
    :param user_id: ID of the user
    :return: Rendered HTML page with movie list or redirect
    """
    if request.method == 'POST':
        try:
            title = request.form.get('title')
            year = request.form.get('year')
            if not title:
                raise ValueError('Name is required')

            data_manager.add_movie(user_id, title, year)
        except ValueError as e:
            print(f"Value Error: {e}")
        except APIError as e:
            print(f"API Error: {e}")

        return redirect(url_for('handle_user_movies', user_id=user_id))
    # get request

    movies = data_manager.get_user_movies(user_id)

    user = data_manager.get_user(user_id)

    return render_template("movies.html", movies=movies, user=user)


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    """
    Updates the title of a movie.
    :param user_id: ID of the user
    :param movie_id: ID of the movie to update
    :return: Redirect to user's movie list
    """
    new_title = request.form.get('new_title')

    data_manager.update_movie_title(movie_id, new_title)
    return redirect(url_for('handle_user_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_user_movie(user_id, movie_id):
    """
    Deletes a movie from the database.
    :param user_id: ID of the user
    :param movie_id: ID of the movie to delete
    :return: Redirect to user's movie list
    """
    data_manager.delete_movie(movie_id)

    return redirect(url_for('handle_user_movies', user_id=user_id))


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors and displays a custom error page.
    :param e: Exception object of the 404 error
    :return: Rendered 404 error page with HTTP status 404
    """
    return render_template("404.html"), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run()