from src.clients.json_placeholder import JSONPlaceholderClient

client = JSONPlaceholderClient()

response = client.get_posts()

posts = response.json()

print(type(posts))
print(len(posts))
print(type(posts[0]))
print(posts[0])
print(posts[0]["title"])
# print("=" * 50)
# print("STATUS CODE")
# print(response.status_code)

# print("=" * 50)
# print("OK?")
# print(response.ok)

# print("=" * 50)
# print("HEADERS")
# print(response.headers)

# print("=" * 50)
# print("ENCODING")
# print(response.encoding)

# print("=" * 50)
# print("ELAPSED")
# print(response.elapsed)

# print("=" * 50)
# print("TEXT")
# print(response.text)

# print("=" * 50)
# print("JSON")
# print(response.json())

# print("=" * 50)
# print("TYPE")
# print(type(response.json()))

# data = response.json()

# print(data["id"])
# print(data["userId"])
# print(data["title"])
# print(data["body"])

