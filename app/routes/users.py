from flask import Blueprint

PREFIX = "users"

USER_BLUEPRINT = Blueprint(PREFIX, __name__)


@USER_BLUEPRINT.route("/", methods=["GET"])
def all():
    return "Hello World!"
