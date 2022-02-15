from flask_restx import Resource, Namespace
from setup_db import db
from dao.model.genres_model import Genre, GenreSchema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genre = db.session.query(Genre).all()
        return GenreSchema(many=True).dump(all_genre), 200


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid: int):
        try:
            genre = db.session.query(Genre).filter(Genre.id == uid).one()
            return GenreSchema().dump(genre), 200
        except Exception as e:
            return str(e), 404
