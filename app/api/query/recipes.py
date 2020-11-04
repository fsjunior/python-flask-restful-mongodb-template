from typing import Type

from app.api.exceptions.recipes import RecipeNotFound
from app.api.query.common import find_by_id
from app.model.recipes import Recipe


def find_recipe_by_id(doc_class: Type[Recipe], doc_id: str) -> Recipe:
    return find_by_id(doc_class, doc_id, RecipeNotFound)
