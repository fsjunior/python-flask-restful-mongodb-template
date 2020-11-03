from marshmallow import EXCLUDE, Schema, fields


class RecipeSchema(Schema):
    id = fields.String(dump_only=True, description="Recipe ID")
    title = fields.String(required=True, description="Title of the recipe")
    ingredients = fields.List(fields.String(required=True), description="Ingredients of the recipe")
    howto = fields.String(required=True, description="How-to bake the recipe")

    class Meta:
        restrict = True


class RecipeQueryArgsSchema(Schema):
    title = fields.String(required=False, description="Title of the recipe")

    class Meta:
        # This is needed otherwise the schema validation will
        # fail with the pagination parameters
        unknown = EXCLUDE
