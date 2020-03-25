from app import app, db
from flask import jsonify
from .defaultExceptions import DefaultException


@app.errorhandler(DefaultException)
def not_found_error(error):
    response = jsonify(error.toDict())
    response.status_code = error.status_code

    return response
