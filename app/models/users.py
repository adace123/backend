from app import db
from .model import Model, MetaModel


class User(db.Model, Model, metaclass=MetaModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())

    def __init__(self, email, password):
        self.email = email
        self.password = password
