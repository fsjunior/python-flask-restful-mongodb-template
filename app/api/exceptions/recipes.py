from werkzeug.exceptions import HTTPException


class RecipeNotFound(HTTPException):
    code = 404
    data = {"message": "Recipe not found"}
