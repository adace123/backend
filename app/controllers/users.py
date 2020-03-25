from flask.json import jsonify
from app.repositories import UserRepository
from ..exceptions import DefaultException


class UserController:
    @staticmethod
    def all():
        users = UserRepository.all()

        return jsonify({"users": users.json})

    @staticmethod
    def get(email):
        try:
            user = UserRepository.get(email)

            print(user)

            return jsonify({"user": user.json})
        except DefaultException as error:
            return jsonify({"error": error})
