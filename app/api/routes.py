from typing import List

from flask import Flask
from flask_smorest import Api, Blueprint

from app.api.rest.recipes import api as recipes_api_v1


# mypy still does not support PEP 585 which allows
# annotations like list[Blueprint] in Python ^3.9
def register_routes(app: Flask, routes: List[Blueprint]):
    api = Api(app)
    for blp in routes:
        api.register_blueprint(blp)


def configure_routes(app: Flask):

    routes = [recipes_api_v1]
    register_routes(app, routes)
