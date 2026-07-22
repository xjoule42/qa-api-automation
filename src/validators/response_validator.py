class ResponseValidator:

    @staticmethod
    def validate_post(post):
        
        assert isinstance(post, dict)

        assert isinstance(post["id"], int)
        assert isinstance(post["userId"], int)
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)