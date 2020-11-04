from werkzeug.exceptions import HTTPException


class InvalidObjectIdException(HTTPException):
    code = 400
    data = {"message": "Malformed ID"}
