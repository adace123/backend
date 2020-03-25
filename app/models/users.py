from app import db
from .model import Model
from datetime import datetime
from app import db


class User(Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())

    _default_fields = [
        'email',
    ]

    _hidden_fields = [
        'password'
    ]

    _readonly_fields = [

    ]
