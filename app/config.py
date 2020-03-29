import os

SQLITE_BASE_URI = f"sqlite:///{os.path.abspath(os.path.dirname(__file__))}"

class Config(object):
    API_PREFIX = "api"
    DEBUG = "DEV"
    HOST = "http://localhost"
    PORT = 3000

    # Database
    LOCAL_DB = "LOCAL"
    SQLITE_DEV_URI = os.path.join(SQLITE_BASE_URI, "app.db")    
    SQLITE_TEST_URI = os.path.join(SQLITE_BASE_URI, "test.db")

    SQLALCHEMY_DATABASE_URI = SQLITE_DEV_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
