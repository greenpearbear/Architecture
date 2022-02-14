from flask import Flask
from flask_restx import Api

from config import Config
# from dao.model import movies_model, directors_model, genres_model
from setup_db import db
from views.movies_views import movies_ns
from views.directors_views import directors_ns
from views.genres_views import genres_ns


def create_app(config_object: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()

    return application


def configurate_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configurate_app(app)
    app.run(host="localhost", port=10001)
