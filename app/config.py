import os
from dotenv import load_dotenv

load_dotenv()
SQLITE_BASE_URI = f"sqlite:///{os.path.abspath(os.path.dirname(__file__))}"

class Config(object):
    API_PREFIX = os.environ['API_PREFIX']
    DEBUG = os.environ['DEBUG']
    HOST = os.environ['HOST']
    PORT = os.environ['PORT']

    # Database
    LOCAL_DB = os.environ['LOCAL_DB']
    SQLITE_DEV_URI = os.path.join(SQLITE_BASE_URI, "app.db")    
    SQLITE_TEST_URI = os.path.join(SQLITE_BASE_URI, "test.db")

    SQLALCHEMY_DATABASE_URI = SQLITE_DEV_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
