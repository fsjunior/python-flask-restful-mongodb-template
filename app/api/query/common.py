from typing import Type

from bson import ObjectId
from flask_mongoengine import Document
from werkzeug.exceptions import NotFound

from app.api.exceptions.common import InvalidObjectIdException


def _validate_objectid(doc_id: str):
    try:
        ObjectId(doc_id)
    except Exception as ex:
        raise InvalidObjectIdException() from ex


def find_by_id(doc_class: Type[Document], doc_id: str, not_found_exception: Type[Exception] = NotFound) -> Document:
    _validate_objectid(doc_id)

    doc = doc_class.objects(id=doc_id)

    if not doc:
        raise not_found_exception()
    return doc
