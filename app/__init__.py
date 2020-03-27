from flask import Flask
from flask.blueprints import Blueprint
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
swagger = Swagger(app)

from app import routes

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(
            blueprint, url_prefix="/" + Config.API_PREFIX + "/" + blueprint.name
        )
