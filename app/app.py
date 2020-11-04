from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

from app.api.routes import configure_routes
from app.cache import configure_cache


def create_app(testing=False):
    app = Flask("python-flask-restful-seed")
    app.config.from_object("app.config.Configuration")

    if testing is True:
        app.config["TESTING"] = True

    configure_cors(app)
    configure_marshmallow(app)
    configure_routes(app)
    configure_cache(app)
    configure_mongodb(app)

    return app


def configure_cors(app):
    CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "False", "expose_headers": ["X-Pagination"]}})


def configure_marshmallow(app: Flask):
    Marshmallow(app)


def configure_mongodb(app: Flask):
    MongoEngine(app)
