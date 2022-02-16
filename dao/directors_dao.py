from dao.model.directors_model import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Director).filter(Director.id == uid).one()

    def get_all(self):
        return self.session.query(Director).all()
