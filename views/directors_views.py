from flask_restx import Resource, Namespace
from flask import request
from marshmallow import Schema, fields
from setup_db import db

directors_ns = Namespace('directors')


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = db.session.query(Director).all()
        return DirectorSchema(many=True).dump(all_directors), 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)

        with db.session.begin():
            db.session.add(new_director)

        return "", 201


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid: int):
        try:
            director = db.session.query(Director).filter(Director.id == uid).one()
            return DirectorSchema().dump(director), 200
        except Exception as e:
            return str(e), 404

    def put(self, uid: int):
        try:
            req_json = request.json
            director = db.session.query(Director).filter(Director.id == uid).one()
            director.id = req_json.get('id')
            director.name = req_json.get('name')

            with db.session.begin():
                db.session.add(director)

            return "", 200
        except Exception as e:
            return str(e), 404

    def delete(self, uid: int):
        try:
            director = db.session.query(Director).filter(Director.id == uid).one()

            with db.session.begin():
                db.session.delete(director)
            return "", 204
        except Exception as e:
            return str(e), 404
