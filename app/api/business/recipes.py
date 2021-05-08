from app.api.business.common import find_by_id
from app.api.exceptions.recipes import RecipeNotFound
from app.model.recipes import Recipe


def find_recipe_by_id(doc_id: str) -> Recipe:
    return find_by_id(Recipe, doc_id, RecipeNotFound)
