from http import HTTPStatus

import pytest

from app.model.recipes import Recipe


class TestRecipe:
    @classmethod
    def setup_class(cls):
        Recipe.drop_collection()

    @pytest.fixture()
    def new_recipe(self):
        return {"title": "ovo cozido", "ingredients": ["ovo", "água"], "howto": "cozinhe o ovo na água"}

    @pytest.fixture()
    def document_recipe(self):
        recipe = Recipe(title="ovo frito", ingredients=["ovo", "óleo"], howto="frite o ovo na frigideira")
        return recipe.save()

    def test_should_post_recipe(self, client, new_recipe):
        response = client.post(
            "/api/v1/recipes",
            json=new_recipe,
        )
        assert response.status_code == HTTPStatus.CREATED

        info_recipe = response.json
        assert info_recipe
        assert "id" in info_recipe
        assert info_recipe["id"] is not None
        assert "title" in info_recipe
        assert info_recipe["title"] == new_recipe["title"]
        assert info_recipe["howto"] is not None
        assert info_recipe["howto"] == new_recipe["howto"]
        assert info_recipe["ingredients"] is not None
        assert type(info_recipe["ingredients"]) is list
        assert sorted(info_recipe["ingredients"]) == sorted(new_recipe["ingredients"])

        new_recipe_document = Recipe.objects(id=info_recipe["id"]).first()
        assert new_recipe_document is not None

        assert new_recipe_document.title == new_recipe["title"]

    def test_should_get_recipe_by_id(self, client, document_recipe):
        response = client.get(f"/api/v1/recipes/{document_recipe.id}")
        assert response.status_code == HTTPStatus.OK

        info_recipe = response.json
        assert info_recipe
        assert "id" in info_recipe
        assert info_recipe["id"] is not None
        assert "title" in info_recipe
        assert info_recipe["title"] == document_recipe.title
        assert info_recipe["howto"] is not None
        assert info_recipe["howto"] == document_recipe.howto
        assert info_recipe["ingredients"] is not None
        assert type(info_recipe["ingredients"]) is list
        assert sorted(info_recipe["ingredients"]) == sorted(document_recipe.ingredients)

    def test_should_not_get_recipe_with_nonexistent_id(self, client):
        # fake id
        response = client.get("/api/v1/recipes/5f95ca454ff087dd3e3eae91")
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_should_not_get_recipe_with_wrong_id(self, client):
        # wrong id
        response = client.get("/api/v1/recipes/wrong_id")
        assert response.status_code == HTTPStatus.BAD_REQUEST
        response_json = response.json

        assert "code" in response_json
        assert "message" in response_json

    def test_should_update_recipe_by_id(self, client, document_recipe):
        response = client.get(f"/api/v1/recipes/{document_recipe.id}")
        assert response.status_code == HTTPStatus.OK

        recipe = response.json

        del recipe["id"]
        recipe["ingredients"].append("sal")
        recipe["howto"] = "frite o ovo na frigideira. sal a gosto"

        response = client.put(f"/api/v1/recipes/{document_recipe.id}", json=recipe)

        assert response.status_code == HTTPStatus.OK

        info_recipe = response.json

        assert info_recipe
        assert "id" in info_recipe
        assert info_recipe["id"] is not None
        assert "title" in info_recipe
        assert info_recipe["title"] == recipe["title"]
        assert info_recipe["howto"] is not None
        assert info_recipe["howto"] == recipe["howto"]
        assert info_recipe["ingredients"] is not None
        assert type(info_recipe["ingredients"]) is list
        assert sorted(info_recipe["ingredients"]) == sorted(recipe["ingredients"])

    def test_should_delete_recipe_by_id(self, client, document_recipe):
        response = client.delete(f"/api/v1/recipes/{document_recipe.id}")
        assert response.status_code == HTTPStatus.NO_CONTENT

    def test_should_get_all_recipes(self, client, document_recipe):
        # fake id
        response = client.get("/api/v1/recipes")
        assert response.status_code == HTTPStatus.OK
        assert "X-Pagination" in response.headers

        info_recipes = response.json
        assert info_recipes
        assert type(info_recipes) is list
        assert any(["id" in recipe for recipe in info_recipes])
        assert any([recipe["id"] == str(document_recipe.id) for recipe in info_recipes])
        assert any([recipe["title"] == document_recipe.title for recipe in info_recipes])
