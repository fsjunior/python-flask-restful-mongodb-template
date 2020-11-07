from app.common import settings


class FlaskConfiguration:
    ENV = settings.app_env
    DEBUG = ENV == "development"
    API_TITLE = settings.app_name
    API_VERSION = settings.app_version

    MONGODB_SETTINGS = {
        "host": settings.mongodb_uri,
    }

    OPENAPI_VERSION = settings.openapi_version
    OPENAPI_URL_PREFIX = settings.openapi_url_prefix

    OPENAPI_SWAGGER_UI_PATH = settings.openapi_swagger_ui_path
    OPENAPI_SWAGGER_UI_URL = settings.openapi_swagger_ui_url

    OPENAPI_REDOC_PATH = settings.openapi_redoc_path
    OPENAPI_REDOC_URL = settings.openapi_redoc_url

    API_SPEC_OPTIONS = {
        "info": {"title": API_TITLE, "description": settings.app_description},
    }
