from models import db, User, Movie



class DataManager:
    def __init__(self):
        db.create_all()

    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def create_movie(self, title, year, director, poster_url, user):
        new_movie = Movie(
            title=title,
            year=year,
            director=director,
            poster_url=poster_url,
            user_id = user)
        db.session.add(new_movie)
        db.session.commit()

