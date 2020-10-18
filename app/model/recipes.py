from flask_mongoengine import Document
from mongoengine import ListField, StringField


class Recipe(Document):
    title = StringField(required=True)
    ingredients = ListField(StringField(), required=True)
    howto = StringField(required=True)
