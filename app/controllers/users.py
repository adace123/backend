from flask.json import jsonify
from app.repositories import UserRepository
from ..exceptions import DefaultException


class UserController:
    @staticmethod
    def all():
        users = UserRepository.all()

        return jsonify({"users": list(map(lambda user: user.json, users))})

    @staticmethod
    def get(email):
        try:
            user = UserRepository.get(email)

            return jsonify({"user": user.json})
        except DefaultException as error:
            return jsonify({"error": error})

    @staticmethod
    def update(model_id, input_data):
        if model_id is None:
            return jsonify({"error": "User not found"}, status_code=404)

        try:
            email = input_data['email']
        except Exception:
            return jsonify({"error": "Email can not be empty"}, status_code=422)

        try:
            password = input_data['password']
        except Exception:
            password = None

        if password is not None:
            try:
                password_confirmation = input_data['password_confirmation']
            except Exception:
                return jsonify({"error": "Password and confirmation are not the same"}, status_code=422)
        else:
            password_confirmation = None

        try:
            user = UserRepository.update(
                model_id=model_id,
                email=email, password=password,
                password_confirmation=password_confirmation
            )

            return jsonify({"updated": user.json})
        except DefaultException as error:
            return jsonify({"error": error})
