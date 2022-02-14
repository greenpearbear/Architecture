from flask_restx import Resource, Namespace
from flask import request
from setup_db import db
from dao.model.genres_model import GenreSchema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genre = db.session.query(Genre).all()
        return GenreSchema(many=True).dump(all_genre), 200

    def post(self):
        req_json = request.json
        genre = Genre(**req_json)

        with db.session.begin():
            db.session.add(genre)
        return "", 201


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid: int):
        try:
            genre = db.session.query(Genre).filter(Genre.id == uid).one()
            return GenreSchema().dump(genre), 200
        except Exception as e:
            return str(e), 404

    def put(self, uid: int):
        try:
            req_json = request.json
            genre = db.session.query(Genre).filter(Genre.id == uid).one()
            genre.id = req_json.get('id')
            genre.name = req_json.get('name')

            with db.session.begin():
                db.session.add(genre)
            return "", 200
        except Exception as e:
            return str(e), 404

    def delete(self, uid: int):
        try:
            genre = db.session.query(Genre).filter(Genre.id == uid).one()

            with db.session.begin():
                db.session.delete(genre)
            return "", 204

        except Exception as e:
            return str(e), 404