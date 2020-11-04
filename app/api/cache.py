from flask import Flask
from flask_caching import Cache

cache = Cache(config={"CACHE_TYPE": "simple"})


def configure_cache(app: Flask):
    cache.init_app(app)
