import pytest

from app.api.business.common import _validate_objectid


class TestCommon:
    def test_if_valid_object_id(self):
        _validate_objectid("5f960d555042a76847bfa0c8")

    def test_if_invalid_object_id(self):
        with pytest.raises(Exception):
            _validate_objectid("fuba")
