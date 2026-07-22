import pytest

@pytest.mark.parametrize("post_id",[1,5,10,25,100])
def test_get_post_by_id_returns_200(client, post_id):
    response = client.get_post(post_id)
    assert response.status_code == 200
