import os
from typing import Any

from dotenv import load_dotenv


class EnvironmentVariableNotFoundException(Exception):
    pass


class Settings:
    def __init__(self):
        load_dotenv(verbose=True)

    @staticmethod
    def _get_env(key: str, type_name: type, default: Any = None) -> Any:
        value = os.getenv(key, default)
        if value is None:
            raise EnvironmentVariableNotFoundException(f"{key} was not defined")
        return type_name(value)

    @property
    def app_name(self) -> str:
        return "Flask Restful Seed"

    @property
    def app_version(self) -> str:
        return "0.1.0"

    @property
    def app_port(self) -> int:
        return Settings._get_env("APP_PORT", int, 8080)

    # Mongo Properties
    @property
    def mongodb_uri(self) -> str:
        return Settings._get_env("MONGODB_URI", str)
