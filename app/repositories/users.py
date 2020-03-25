from app.models import User
from ..exceptions import DefaultException


class UserRepository:
    @staticmethod
    def all():
        return User.query.all()

    @staticmethod
    def get(email):
        user = User.query.filter_by(email=email).one()

        if user is None:
            raise DefaultException("User could not be found", status_code=404)

        return user

    @staticmethod
    def save(email, password, password_confirmation):
        if password != password_confirmation:
            raise DefaultException("Passwords are not the same", status_code=422)

        user = User(email=email, password=password)
        return user.save()

    @staticmethod
    def update(email, password=None, password_confirmation=None):
        user = UserRepository.get(email)

        if user is None:
            raise DefaultException("User could not be found", status_code=404)

        user.email = email

        if password is not None:
            if password == password_confirmation:
                user.password = password

        return user.save()
