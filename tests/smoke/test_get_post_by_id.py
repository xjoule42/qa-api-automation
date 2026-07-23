import pytest
from src.validators.response_validator import ResponseValidator
from tests.schemas.post_schema import POST_SCHEMA
from src.validators.schema_validator import SchemaValidator
from src.helpers.assertions import assert_status_code

@pytest.mark.parametrize("post_id",[1,5,10,25,100])
def test_get_post_by_id_returns_200(client, post_id):
    
    response = client.get_post(post_id)
    
    assert_status_code(response, 200)

    data = response.json()
    ResponseValidator.validate_post(data)
    SchemaValidator.validate_schema(data, POST_SCHEMA)