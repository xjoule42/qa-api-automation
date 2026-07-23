from tests.fixtures.post_payloads import PATCH_POST

def test_patch_post(client):

    response = client.patch_post(1, PATCH_POST)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == PATCH_POST["title"]