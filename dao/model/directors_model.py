from setup_db import db


class Director(db.Model):
    __table_name__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))