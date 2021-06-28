from flask.views import MethodView
from flask_smorest import Blueprint
from flask_smorest.pagination import PaginationParameters

from app.api.business.recipes import find_recipe_by_id
from app.api.schema.recipes import RecipeQueryArgsSchema, RecipeSchema
from app.cache import cache
from app.model.recipes import Recipe

api = Blueprint(
    "Recipes API",
    __name__,
    url_prefix="/api/v1/recipes",
    description="In this API you can create, search or update recipes.",
)


@api.route("")
class Recipes(MethodView):
    @classmethod
    @api.arguments(RecipeQueryArgsSchema, location="query")
    @api.paginate()
    @api.response(200, RecipeSchema(many=True))
    def get(cls, recipe_args: dict, pagination_parameters: PaginationParameters):
        """List recipes"""
        result = Recipe.objects(**recipe_args).paginate(pagination_parameters.page, pagination_parameters.page_size)
        pagination_parameters.item_count = result.total
        return result.items

    @classmethod
    @api.arguments(RecipeSchema)
    @api.response(201, RecipeSchema)
    def post(cls, recipe_data: dict):
        """Add a new recipe"""
        item = Recipe(**recipe_data)
        item.save()
        return item


@api.route("/<recipe_id>")
class RecipeById(MethodView):
    # I use a classmethod instead of a object because it is
    # not recomendded to use memoization with objects
    # (as the `self` reference could always change)
    # see: https://flask-caching.readthedocs.io/en/latest/#memoization
    @staticmethod
    @api.response(200, RecipeSchema)
    @cache.memoize(timeout=30)
    def get(recipe_id: str):
        """Get recipe by ID"""
        return find_recipe_by_id(recipe_id).first()

    @staticmethod
    @api.arguments(RecipeSchema)
    @api.response(200, RecipeSchema)
    def put(recipe_data: dict, recipe_id: str):
        """Update existing recipe"""
        item = find_recipe_by_id(recipe_id).first()
        item.update(**recipe_data)
        item.save()
        return find_recipe_by_id(recipe_id).first()

    @staticmethod
    @api.response(204)
    def delete(recipe_id: str):
        """Delete recipe"""
        find_recipe_by_id(recipe_id).delete()
