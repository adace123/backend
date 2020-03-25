from flask import Blueprint
from app.controllers import UserController

PREFIX = "users"

USER_BLUEPRINT = Blueprint(PREFIX, __name__)


@USER_BLUEPRINT.route("/", methods=["GET"])
def all():
    return UserController.all()


@USER_BLUEPRINT.route("/<email>", methods=["GET"])
def get(email):
    return UserController.get(email)
