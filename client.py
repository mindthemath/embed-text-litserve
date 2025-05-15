import requests

data = {
    "input": "some text to embed",
    "model": "nomic-embed-text-v1.5",
}
url = "http://localhost:8000/v1/embeddings"
response = requests.post(url, json=data)
print(response.json())
