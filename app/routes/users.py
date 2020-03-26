from flask import Blueprint, request, abort, jsonify
from app.controllers import UserController

PREFIX = "users"

USER_BLUEPRINT = Blueprint(PREFIX, __name__)


@USER_BLUEPRINT.route("/", methods=["GET"])
def all():
    return UserController.all()


@USER_BLUEPRINT.route("/<model_id>", methods=["GET"])
def get(model_id):
    return UserController.get(model_id)


@USER_BLUEPRINT.route("/", methods=["POST"])
def create():
    try:
        input_data = request.get_json(force=True)
    except Exception as error:
        return jsonify({"error": "Request data must be a JSON object"}), 404

    if not isinstance(input_data, dict):
        return jsonify({"error": "Request data must be a JSON object"}), 400

    return UserController.create(input_data)


@USER_BLUEPRINT.route("/<string:model_id>", methods=["PUT"])
def update(model_id):
    try:
        input_data = request.get_json(force=True)
    except Exception as error:
        return jsonify({"error": "Request data must be a JSON object"}), 404

    if not isinstance(input_data, dict):
        return jsonify({"error": "Request data must be a JSON object"}), 404

    return UserController.update(model_id, input_data)


@USER_BLUEPRINT.route("/<string:model_id>", methods=["DELETE"])
def delete(model_id):
    return UserController.delete(model_id)
