import os
from typing import Any

import toml
from dotenv import load_dotenv


class EnvironmentVariableNotFoundException(Exception):
    pass


class Settings:
    def __init__(self):
        load_dotenv(verbose=True)
        self.py_project = toml.load("pyproject.toml")

    @staticmethod
    def _get_env(key: str, type_name: type, default: Any = None) -> Any:
        value = os.getenv(key, default)
        if value is None:
            raise EnvironmentVariableNotFoundException(f"{key} was not defined")
        return type_name(value)

    # Generic App and Flask settings
    @property
    def app_name(self) -> str:
        return self.py_project["tool"]["poetry"]["name"]

    @property
    def app_version(self) -> str:
        return self.py_project["tool"]["poetry"]["version"]

    @property
    def app_description(self) -> str:
        return self.py_project["tool"]["poetry"]["description"]

    @property
    def app_port(self) -> int:
        return self._get_env("APP_PORT", int, 80)

    @property
    def app_env(self) -> str:
        return self._get_env("FLASK_ENV", str, "development")

    # Mongo Settings

    @property
    def mongodb_uri(self) -> str:
        return self._get_env("MONGODB_URI", str)

    # OpenAPI Settings

    @property
    def openapi_version(self) -> str:
        return "3.0.3"

    @property
    def openapi_url_prefix(self) -> str:
        return self._get_env("OPENAPI_URL_PREFIX", str, "/doc")

    @property
    def openapi_swagger_ui_path(self) -> str:
        return self._get_env("OPENAPI_SWAGGER_UI_PATH", str, "/swagger")

    @property
    def openapi_swagger_ui_url(self) -> str:
        return self._get_env("OPENAPI_SWAGGER_UI_URL", str, "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.36.1/")

    @property
    def openapi_redoc_path(self) -> str:
        return self._get_env("OPENAPI_REDOC_PATH", str, "/redoc")

    @property
    def openapi_redoc_url(self) -> str:
        return self._get_env(
            "OPENAPI_REDOC_URL", str, "https://cdn.jsdelivr.net/npm/redoc@2.0.0-rc.45/bundles/redoc.standalone.js"
        )
