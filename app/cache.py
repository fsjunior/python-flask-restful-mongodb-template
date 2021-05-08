from flask import Flask
from flask_caching import Cache

cache = Cache(config={"CACHE_TYPE": "SimpleCache"})


def configure_cache(app: Flask):
    cache.init_app(app)
