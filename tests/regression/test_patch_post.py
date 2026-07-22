def test_patch_post(client):

    payload = {
        "title": "Patched title"
    }

    response = client.patch_post(1, payload)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]