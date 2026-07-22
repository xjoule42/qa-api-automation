from src.clients.base_client import BaseClient


class JSONPlaceholderClient(BaseClient):

    def get_posts(self, params=None):

        return self.get("/posts", params=params)

    def get_post(self, post_id):

        return self.get(f"/posts/{post_id}")

    def create_post(self, payload):

        return self.post("/posts", payload)

    def update_post(self, post_id, payload):

        return self.put(f"/posts/{post_id}", payload)

    def patch_post(self, post_id, payload):

        return self.patch(f"/posts/{post_id}", payload)

    def delete_post(self, post_id):

        return self.delete(f"/posts/{post_id}")