import pytest


@pytest.fixture(scope="session")
def app():
    from app.app import create_app

    app = create_app()
    app.config["TESTING"] = True

    return app
