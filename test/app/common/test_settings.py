import pytest

from app.common import settings
from app.common.settings import EnvironmentVariableNotFoundException


class TestSettings:
    def test_should_get_env_var(self, mocker):
        mocker.patch("os.getenv", lambda x, y: 123456)
        assert settings.app_port == 123456

    def test_should_raise_exception(self, mocker):
        mocker.patch("os.getenv", lambda x, y: None)
        with pytest.raises(EnvironmentVariableNotFoundException):
            settings.app_port
