def test_delete_post(client):

    response = client.delete_post(1)

    assert response.status_code == 200

    assert response.text == "{}"
    