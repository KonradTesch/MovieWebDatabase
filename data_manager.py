from sqlalchemy.sql.functions import user

from models import db, User, Movie
import os
import requests
from dotenv import load_dotenv

api_key = ""

def set_api_key():
    """
    Load the api key from the env file and sets the global variable.
    :return:
    """
    load_dotenv()
    global api_key
    api_key = os.getenv("API_KEY")


class APIError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"APIError: {message}")

    def __str__(self):
        return f"APIError: {self.message}"

class DataManager:

    @staticmethod
    def create_user(name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def create_movie(self, title, year, director, poster_url, user_id):
        new_movie = Movie(
            title=title,
            year=year,
            director=director,
            poster_url=poster_url,
            user_id = user_id)
        db.session.add(new_movie)
        db.session.commit()

    def delete_movie(self, movie_id):
        db.session.query(Movie).filter_by(id=movie_id).delete()
        db.session.commit()

    def get_users(self):
        users = db.session.query(User).all()
        return users


    def get_user_movies(self, user_id):
        movies = db.session.query(Movie).filter_by(user_id=user_id).all()

    def delete_user_movies(self,user_id, movie_id):
        db.session.query(Movie).filter_by(id=movie_id, user_id=user_id).delete()

    def add_movie(self,user_id, title, year = None):

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

        self.create_movie(title=title, year=year, director=director,poster_url=poster_url, user_id=user_id)



