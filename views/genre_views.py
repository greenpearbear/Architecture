from flask_restx import Resource, Namespace
from dao.model.genre_model import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genre = genre_service.get_all()
        return GenreSchema(many=True).dump(all_genre), 200


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid: int):
        try:
            genre = genre_service.get_one(uid)
            return GenreSchema().dump(genre), 200
        except Exception as e:
            return str(e), 404
