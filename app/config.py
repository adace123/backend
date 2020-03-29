import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    API_PREFIX = os.environ['API_PREFIX']
    DEBUG = os.environ['DEBUG']
    HOST = os.environ['HOST']
    PORT = os.environ['PORT']

    # Database
    LOCAL_DB = os.environ['LOCAL_DB']
    SQLITE_URI = "sqlite:///" + os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "app.db"
    )

    SQLALCHEMY_DATABASE_URI = SQLITE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
