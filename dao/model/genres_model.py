from setup_db import db


class Genre(db.Model):
    __table_name__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
