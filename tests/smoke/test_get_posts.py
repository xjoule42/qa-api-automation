# Status Code
def test_get_posts_returns_status_200(client):
    response = client.get_posts()
    assert response.status_code == 200

# Headers
def test_get_posts_returns_json(client):
    response = client.get_posts()
    assert response.headers["Content-Type"] == \
          "application/json; charset=utf-8"

# JSON
def test_get_posts_returns_list(client):
    response = client.get_posts()
    data = response.json()
    assert isinstance(data, list)

# Post is not empty
def test_get_posts_is_not_empty(client):

    response = client.get_posts()

    data = response.json()

    assert len(data) > 0

# Validate Expected fields
def test_first_post_contains_expected_fields(client):
    response = client.get_posts()
    first_post = response.json()[0]

    assert "id" in first_post
    assert "userId" in first_post
    assert "title" in first_post
    assert "body" in first_post