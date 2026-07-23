from tests.fixtures.post_payloads import UPDATED_POST

def test_update_post(client):

    response = client.update_post(1, UPDATED_POST)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == UPDATED_POST["title"]
    assert data["body"] == UPDATED_POST["body"]
    assert data["userId"] == UPDATED_POST["userId"]