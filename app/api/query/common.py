from bson import ObjectId
from flask_mongoengine import Document
from werkzeug.exceptions import NotFound


def validate_objectid(doc_id: str):
    try:
        ObjectId(doc_id)
    except Exception:
        raise NotFound()


def find_by_id(doc_class: Document, doc_id: str) -> Document:
    validate_objectid(doc_id)

    doc = doc_class.objects(id=doc_id)

    if not doc:
        raise NotFound()
    return doc
