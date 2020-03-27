from flask import Blueprint, request, abort, jsonify
from app.controllers import UserController

PREFIX = "users"

USER_BLUEPRINT = Blueprint(PREFIX, __name__)


@USER_BLUEPRINT.route("/", methods=["GET"])
def all():
    """
    Retrieving a list of users
    ---
    definitions:
        User:
            type: object
            properties:
                id:
                    type: integer
                email:
                    type: string
    responses:
        200:
            description: Display a list of users
            schema:
                $ref: '#/definitions/User'
    """
    return UserController.all()


@USER_BLUEPRINT.route("/<model_id>", methods=["GET"])
def get(model_id):
    """
    Retrieve a single user by ID
    ---
    parameters:
        - name: model_id
          in: path
          type: string
          description: The ID of the user
          required: true
    definitions:
        User:
            type: object
            properties:
                id:
                    type: integer
                email:
                    type: string
    responses:
        200:
            description: Display a single user
            schema:
                $ref: '#/definitions/User'
        404:
            description: User could not be found
            schema:
                type: string
                example: { "message": "User could not be found"}
    """
    return UserController.get(model_id)


@USER_BLUEPRINT.route("/", methods=["POST"])
def create():
    """
    Create a new user
    ---
    parameters:
        - name: body
          in: body
          required: true
          schema:
            type: object
            properties:
                email:
                    type: string
                password:
                    type: string
                password_confirmation:
                    type: string
            required:
                - email
                - password
                - password_confirmation
    responses:
        201:
            description: User has been created
            schema:
                $ref: '#/definitions/User'
        422:
            description: Form Validation Error
            schema:
                type: string
                example: { "message": "A password is required"}
        400:
            description: Bad Request
            schema:
                type: string
                example: { "message": "Request data must be a JSON object"}
    """
    try:
        input_data = request.get_json(force=True)
    except Exception as error:
        return jsonify({"error": "Request data must be a JSON object"}), 400

    if not isinstance(input_data, dict):
        return jsonify({"error": "Request data must be a JSON object"}), 400

    return UserController.create(input_data)


@USER_BLUEPRINT.route("/<string:model_id>", methods=["PUT"])
def update(model_id):
    """
        Update an existing User
        ---
        parameters:
            - name: model_id
              in: path
              description: The ID of the user
              required: true
              type: string
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                    email:
                        type: string
                    password:
                        type: string
                    password_confirmation:
                        type: string
                required:
                    - email
        responses:
            200:
                description: User has been updated
                schema:
                    $ref: '#/definitions/User'
            404:
                description: User could not be found
                schema:
                    type: string
                    example: { "message": "User could not be found"}
            422:
                description: Form Validation Error
                schema:
                    type: string
                    example: { "message": "password and confirmation are not the same"}
            400:
                description: Bad Request
                schema:
                    type: string
                    example: { "message": "Request data must be a JSON object"}
        """
    try:
        input_data = request.get_json(force=True)
    except Exception as error:
        return jsonify({"error": "Request data must be a JSON object"}), 400

    if not isinstance(input_data, dict):
        return jsonify({"error": "Request data must be a JSON object"}), 400

    return UserController.update(model_id, input_data)


@USER_BLUEPRINT.route("/<string:model_id>", methods=["DELETE"])
def delete(model_id):
    """
        Delete an existing User
        ---
        parameters:
            - name: model_id
              in: path
              type: string
              description: The ID of the user
              required: true
        definitions:
            User:
                type: object
                properties:
                    id:
                        type: integer
                    email:
                        type: string
        responses:
            200:
                description: Display a single user
                schema:
                    type: string
                    example: { "message": "User has been deleted"}
            404:
                description: User could not be found
                schema:
                    type: string
                    example: { "message": "User could not be found"}
        """
    return UserController.delete(model_id)
