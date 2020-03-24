from flask import Flask
from flask.blueprints import Blueprint
from .config import Config

app = Flask(__name__)

from app import routes

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(
            blueprint, url_prefix="/" + Config.API_PREFIX + "/" + blueprint.name
        )
