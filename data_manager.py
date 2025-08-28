from models import db, User, Movie
import os
import requests
from dotenv import load_dotenv

api_key = ""


def set_api_key():
    """
    Loads the API key from the .env file and sets the global variable.
    :return: None
    """
    load_dotenv()
    global api_key
    api_key = os.getenv("API_KEY")


class APIError(Exception):
    """Custom exception class for API-related errors."""

    def __init__(self, message):
        """
        Initializes a new APIError instance.
        :param message: Error message
        """
        self.message = message
        super().__init__(f"APIError: {message}")

    def __str__(self):
        """
        Returns the string representation of the API error.
        :return: Formatted error message as string
        """
        return f"APIError: {self.message}"


class DataManager:
    """Manages all database operations and API calls for the Movie App."""

    def __init__(self):
        """
        Initializes the DataManager and loads the API key.
        """
        set_api_key()

    def create_user(self, name):
        """
        Creates a new user in the database.

        :param name: Name of the new user
        :return: None
        """
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def create_movie(self, title, year, director, poster_url, user_id):
        """
        Creates a new movie in the database.

        :param title: Movie title
        :param year: Release year of the movie
        :param director: Director of the movie
        :param poster_url: URL to the movie poster
        :param user_id: ID of the user who owns the movie
        :return: None
        """
        new_movie = Movie(
            title=title,
            year=year,
            director=director,
            poster_url=poster_url,
            user_id=user_id)
        db.session.add(new_movie)
        db.session.commit()

    def delete_movie(self, movie_id):
        """
        Deletes a movie from the database.

        :param movie_id: ID of the movie to delete
        :return: None
        """
        db.session.query(Movie).filter_by(id=movie_id).delete()
        db.session.commit()

    def get_users(self):
        """
        Retrieves all users from the database.

        :return: List of all User objects
        """
        users = db.session.query(User).all()
        return users

    def get_user(self, user_id):
        """
        Retrieves a specific user by ID.

        :param user_id: ID of the user to find
        :return: User object or None if not found
        """
        user_data = db.session.query(User).filter_by(id=user_id).first()
        return user_data

    def get_user_movies(self, user_id):
        """
        Retrieves all movies for a specific user.

        :param user_id: ID of the user
        :return: List of all Movie objects belonging to the user
        """
        movies = db.session.query(Movie).filter_by(user_id=user_id).all()
        return movies

    def update_movie_title(self, movie_id, title):
        """
        Updates the title of a movie.

        :param movie_id: ID of the movie to update
        :param title: New title for the movie
        :return: None
        """
        movie = db.session.query(Movie).filter_by(id=movie_id).first()
        movie.title = title
        db.session.commit()

    def add_movie(self, user_id, title, year=None):
        """
        Adds a new movie by fetching movie data from the OMDB API.

        :param user_id: ID of the user to assign the movie to
        :param title: Title of the movie to search for
        :param year: Optional release year for more precise search
        :return: None
        :raises APIError: When the API returns an error or movie is not found
        """
        year_param = f"&y={year}" if year else ""
        url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}{year_param}"

        response = requests.get(url)

        response_data = response.json()

        if response_data.get("Error"):
            error_message = response_data["Error"]
            raise APIError(error_message)

        title = response_data["Title"]
        year = response_data["Year"]
        director = response_data["Director"]
        poster_url = response_data.get("Poster", "")

        self.create_movie(title=title, year=year, director=director, poster_url=poster_url, user_id=user_id)