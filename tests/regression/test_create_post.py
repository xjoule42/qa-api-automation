def test_create_post(client):

    payload = {
        "title": "My first API Test",
        "body": "Created with Pytest",
        "userId": 1
    }

    response = client.create_post(payload)

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    assert "id" in data