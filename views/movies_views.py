from flask_restx import Resource, Namespace
from flask import request
from setup_db import db
from dao.model.movies_model import MovieSchema


movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        genre_id = request.args.get('genre_id')
        director_id = request.args.get('director_id')
        all_movies = db.session.query(Movie).all()
        return MovieSchema(many=True).dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)

        with db.session.begin():
            db.session.add(new_movie)

        return "", 201


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        try:
            movie = db.session.query(Movie).filter(Movie.id == uid).one()
            return MovieSchema().dump(movie), 200

        except Exception as e:
            return str(e), 404

    def put(self, uid: int):
        try:
            movie = db.session.query(Movie).filter(Movie.id == uid).one()
            req_json = request.json
            movie.id = req_json.get("id")
            movie.title = req_json.get("title")
            movie.description = req_json.get("description")
            movie.trailer = req_json.get("trailer")
            movie.year = req_json.get("year")
            movie.rating = req_json.get("rating")
            movie.genre_id = req_json.get("genre_id")
            movie.director_id = req_json.get("director_id")

            with db.session.begin():
                db.session.add(movie)

            return "", 200

        except Exception as e:
            return str(e), 404

    def delete(self, uid: int):
        try:
            movie = db.session.query(Movie).filter(Movie.id == uid).one()

            with db.session.begin():
                db.session.delete(movie)

            return "", 204
        except Exception as e:
            return str(e), 404
