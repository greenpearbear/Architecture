from flask_restx import Resource, Namespace
from flask import request
from dao.model.movies_model import Movie, MovieSchema


movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_dao.get_all()
        return MovieSchema(many=True).dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = movie_dao.post(req_json)
        return new_movie, 201


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        try:
            movie = movie_dao.get_one(uid)
            return MovieSchema().dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, uid: int):
        try:
            req_json = request.json
            movie = movie_dao.put(uid, req_json)
            return MovieSchema().dump(movie), 200
        except Exception as e:
            return str(e), 404

    def delete(self, uid: int):
        try:
            movie = movie_dao.delete(uid)
            return MovieSchema().dump(movie), 204
        except Exception as e:
            return str(e), 404
