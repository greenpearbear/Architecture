from dao.model.movies_model import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, uid):
        return self.session.query(Movie).filter(Movie.id == uid).one()

    def post(self, data):
        movie = Movie(**data)
        with self.session.begin():
            self.session.add(movie)
        return movie

    def put(self, uid, data):
        movie = self.get_one(uid)
        movie.id = data.get("id")
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")
        with self.session.begin():
            self.session.add(movie)
        return movie

    def delete(self, uid):
        movie = self.get_one(uid)
        with self.session.begin():
            self.session.delete(movie)
