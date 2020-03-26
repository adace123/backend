from flask.json import jsonify
from app.repositories import UserRepository
from ..exceptions import DefaultException


class UserController:
    @staticmethod
    def all():
        users = UserRepository.all()

        return jsonify({"users": list(map(lambda user: user.json, users))}), 200

    @staticmethod
    def get(email):
        try:
            user = UserRepository.get(email)

            return jsonify({"user": user.json}), 200
        except DefaultException as error:
            return jsonify({"error": error.message}), error.status_code

    @staticmethod
    def create(input_data):
        try:
            email = input_data["email"]
        except Exception:
            return jsonify({"error": "Email can not be empty"}), 422

        try:
            password = input_data["password"]
        except Exception:
            return jsonify({"error": "Password cannot be empty"}), 422

        if password is not None:
            try:
                password_confirmation = input_data["password_confirmation"]
            except Exception:
                return jsonify(
                    {"error": "Password and confirmation are not the same"}
                ), 422
        else:
            return jsonify(
                {"error": "Password and confirmation are not the same"}
            ), 422

        try:
            user = UserRepository.save(
                email=email,
                password=password,
                password_confirmation=password_confirmation,
            )

            return jsonify({"created": user.json}), 201
        except DefaultException as error:
            return jsonify({"error": error.message}), error.status_code

    @staticmethod
    def update(model_id, input_data):
        if model_id is None:
            return jsonify({"error": "User not found"}), 404

        try:
            email = input_data["email"]
        except Exception:
            return jsonify({"error": "Email can not be empty"}), 422

        try:
            password = input_data["password"]
        except Exception:
            password = None

        if password is not None:
            try:
                password_confirmation = input_data["password_confirmation"]
            except Exception:
                return jsonify(
                    {"error": "Password and confirmation are not the same"}
                ), 422
        else:
            password_confirmation = None

        try:
            user = UserRepository.update(
                model_id=model_id,
                email=email,
                password=password,
                password_confirmation=password_confirmation,
            )

            return jsonify({"updated": user.json}), 200
        except DefaultException as error:
            return jsonify({"error": error.message}), error.status_code
