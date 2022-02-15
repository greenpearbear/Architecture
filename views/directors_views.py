from flask_restx import Resource, Namespace
from setup_db import db
from dao.model.directors_model import Director, DirectorSchema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = db.session.query(Director).all()
        return DirectorSchema(many=True).dump(all_directors), 200


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid: int):
        try:
            director = db.session.query(Director).filter(Director.id == uid).one()
            return DirectorSchema().dump(director), 200
        except Exception as e:
            return str(e), 404
