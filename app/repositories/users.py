from app.models import User
from ..exceptions import DefaultException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


class UserRepository:
    @staticmethod
    def all():
        return User.query.all()

    @staticmethod
    def get(model_id):
        try:
            user = User.query.filter_by(id=model_id).one()
        except NoResultFound:
            raise DefaultException("User could not be found", status_code=404)

        return user

    @staticmethod
    def save(email, password, password_confirmation):
        if password != password_confirmation:
            raise DefaultException("Passwords are not the same", status_code=422)

        user = User(email=email, password=password)
        try:
            user.save()
        except IntegrityError as error:
            raise DefaultException("Email already exists", status_code=422)
        return user

    @staticmethod
    def update(model_id, email, password=None, password_confirmation=None):
        try:
            user = UserRepository.get(model_id)
        except DefaultException as error:
            raise error

        user.email = email

        if password is not None:
            if password == password_confirmation:
                user.password = password

        try:
            user.save()
        except Exception as error:
            raise DefaultException(error, status_code=500)

        return user

    @staticmethod
    def delete(model_id):
        try:
            user = UserRepository.get(model_id)
        except DefaultException as error:
            raise error

        try:
            user.delete()
            return True
        except Exception as error:
            raise DefaultException(error, status_code=500)
