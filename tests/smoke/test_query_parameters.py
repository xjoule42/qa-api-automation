# Query parameters

def test_get_posts_by_user_id(client):
    
    response = client.get_posts(params={"userId": 1})

    assert response.status_code == 200

    posts = response.json()

    assert len(posts) > 0

    for post in posts:
        assert post["userId"] == 1

def test_get_post_by_user_id_and_post_id(client):

    response = client.get_posts(params={
        "userId": 1,
        "id": 1
    })

    assert response.status_code == 200

    posts = response.json()

    assert len(posts) == 1

    assert posts[0]["userId"] == 1
    assert posts[0]["id"] == 1