from flask.views import MethodView
from flask_smorest import Blueprint
from flask_smorest.pagination import PaginationParameters

from app.api.cache import cache
from app.api.query.common import find_by_id
from app.api.schema.recipes import RecipeQueryArgsSchema, RecipeSchema
from app.model.recipes import Recipe

api = Blueprint("api", __name__, url_prefix="/api/v1/recipes", description="Recipe API")


@api.route("")
class Recipes(MethodView):
    @classmethod
    @api.arguments(RecipeQueryArgsSchema, location="query")
    @api.paginate()
    @api.response(RecipeSchema(many=True))
    def get(cls, recipe_args: dict, pagination_parameters: PaginationParameters):
        """List recipes"""
        result = Recipe.objects(**recipe_args).paginate(pagination_parameters.page, pagination_parameters.page_size)
        pagination_parameters.item_count = result.total
        return result.items

    @classmethod
    @api.arguments(RecipeSchema)
    @api.response(RecipeSchema, code=201)
    def post(cls, recipe_data: dict):
        """Add a new recipe"""
        item = Recipe(**recipe_data)
        item.save()
        return item


@api.route("/<recipe_id>")
class RecipeById(MethodView):
    # I use a classmethod instead of a object because it is
    # not recomendded to use memoization with objects
    # (as self reference could always change)
    # see: https://flask-caching.readthedocs.io/en/latest/#memoization
    @classmethod
    @api.response(RecipeSchema)
    @cache.memoize(timeout=30)
    def get(cls, recipe_id: str):
        """Get recipe by ID"""
        return find_by_id(Recipe, recipe_id).first()

    @classmethod
    @api.arguments(RecipeSchema)
    @api.response(RecipeSchema)
    def put(cls, recipe_data: dict, recipe_id: str):
        """Update existing recipe"""
        item = find_by_id(Recipe, recipe_id).first()
        item.update(**recipe_data)
        item.save()
        return find_by_id(Recipe, recipe_id).first()

    @classmethod
    @api.response(code=204)
    def delete(cls, recipe_id: str):
        """Delete recipe"""
        find_by_id(Recipe, recipe_id).delete()
