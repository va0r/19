# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
class Config(object):
    """
    Создание класса-конфигуратора.
    """
    DEBUG = True
    HOST = '127.0.0.19'
    PORT = 10019
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
