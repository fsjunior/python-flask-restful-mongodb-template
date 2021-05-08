from marshmallow import EXCLUDE, Schema, fields


class RecipeSchema(Schema):
    id = fields.String(dump_only=True, metadata={"description": "Recipe ID"})
    title = fields.String(required=True, metadata={"description": "Title of the recipe"})
    ingredients = fields.List(fields.String(required=True), metadata={"description": "Ingredients of the recipe"})
    howto = fields.String(required=True, metadata={"description": "How-to bake the recipe"})

    class Meta:
        restrict = True


class RecipeQueryArgsSchema(Schema):
    title = fields.String(required=False, metadata={"description": "Title of the recipe"})

    class Meta:
        # This is needed otherwise the schema validation will
        # fail with the pagination parameters
        unknown = EXCLUDE
