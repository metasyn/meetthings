import pytest

from meetthings import util

@pytest.mark.parametrize("schema", ["gcal", "meetthings", "meetup"])
def test_load_schema(schema):
    schema = util.load_schema(schema)
    assert isinstance(schema, dict), "load_schema should return a valid dictionary"
    
