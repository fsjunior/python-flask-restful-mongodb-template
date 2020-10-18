"""Default configuration

Use env var to override
"""
import os

from app.common import settings


class Configuration:
    ENV = os.getenv("FLASK_ENV")
    DEBUG = ENV == "development"
    API_TITLE = settings.app_name
    API_VERSION = settings.app_version

    MONGODB_SETTINGS = {
        "host": settings.mongodb_uri,
    }

    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = os.getenv("OPENAPI_URL_PREFIX")

    OPENAPI_SWAGGER_UI_PATH = os.getenv("OPENAPI_SWAGGER_UI_PATH")
    OPENAPI_SWAGGER_UI_URL = os.getenv("OPENAPI_SWAGGER_UI_URL")

    OPENAPI_REDOC_PATH = os.getenv("OPENAPI_REDOC_PATH")
    OPENAPI_REDOC_URL = os.getenv("OPENAPI_REDOC_URL")

    API_SPEC_OPTIONS = {
        "info": {"title": API_TITLE, "description": ""},
    }
