import os


class Config(object):
    API_PREFIX = "api"
    DEBUG = "DEV"
    HOST = "http://localhost"
    PORT = 3000

    # Database
    LOCAL_DB = "LOCAL"
    SQLITE_URI = "sqlite:///" + os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "app.db"
    )

    SQLALCHEMY_DATABASE_URI = SQLITE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
