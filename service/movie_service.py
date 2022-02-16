from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def post(self, data):
        return self.dao.post(data)

    def get_one(self, uid):
        return self.dao.get_one(uid)

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
        self.dao.put(movie)

    def delete(self, uid):
        return self.dao.delete(uid)
