class DefaultException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message

        if status_code is not None:
            self.status_code = status_code

        if payload is not None:
            self.payload = payload

    def to_dict(self):
        error = dict(self.payload or ())
        error["message"] = self.message
        return error
