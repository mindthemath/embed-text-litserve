import requests

data = {
    "input": "some text to embed",
}
url = "http://localhost:8031/embed"
response = requests.post(url, json=data)
out = response.json()

print(out.keys())
print(out["embeddings"][:12])
