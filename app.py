# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from flask import Flask
from flask_restx import Api

from config import Config
from errorhandlers.views import errorhandlers
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(config_object) -> Flask:
    """
    Создание приложения Flask.
    """
    app: Flask = Flask(__name__)
    app.register_blueprint(errorhandlers)
    app.config.from_object(config_object)
    configure_app(app)
    return app


def configure_app(app) -> None:
    """
    Конфигурация приложения Flask.
    """
    db.init_app(app)
    api: Api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


config: Config = Config()
app: Flask = create_app(config)
app.debug = True
app.url_map.strict_slashes = False

if __name__ == '__main__':
    app.run(host=config.HOST,
            port=config.PORT,
            debug=config.DEBUG)
