import requests

data = {
    "input": "Your text string goes here",
    "model": "nomic-embed-text-v1.5",
}
url = "http://localhost:8000/v1/embeddings"
response = requests.post(url, json=data)
print(response.json())
