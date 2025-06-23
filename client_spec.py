import requests

data = {
    "input": "some text to embed",
    "model": "nomic-embed-text-v1.5",
}
url = "http://localhost:8031/v1/embeddings"
response = requests.post(url, json=data)
out = response.json()

print(out.keys())
print(out["data"][0].keys())
print(out["data"][0]["index"])
