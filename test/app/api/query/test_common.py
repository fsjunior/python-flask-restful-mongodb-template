from app.api.query.common import validate_objectid
import pytest


class TestCommon:
    def test_if_valid_object_id(self):
        validate_objectid("5f960d555042a76847bfa0c8")

    def test_if_invalid_object_id(self):
        with pytest.raises(Exception):
            validate_objectid("fuba")
