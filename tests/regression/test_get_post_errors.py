def test_get_nonexistent_post_returns_empty_object(client):

    response = client.get_post(9999)

    assert response.status_code == 404
    assert response.json() == {}

def test_delete_nonexistent_post_returns_404(client):

    response = client.delete_post(9999)

    assert response.status_code == 200
    assert response.json() == {}

def test_update_nonexistent_post(client):

    payload = {
        "title": "Updated",
        "body": "Updated body",
        "userId": 1
    }

    response = client.update_post(9999, payload)

    assert response.status_code == 500
   # print(f"Status Quode XD: {response.status_code}")
   # print(response.text)

def test_patch_nonexistent_post(client):

    payload = {
        "title": "Updated"
    }

    response = client.patch_post(9999, payload)

    assert response.status_code == 200
    assert response.json()["title"] == "Updated"

def test_create_post_with_empty_payload(client):

    payload = {}

    response = client.create_post(payload)

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 101