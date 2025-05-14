from sentence_transformers import SentenceTransformer
import litserve as ls
import os
import numpy as np

# Environment configurations
PORT = int(os.environ.get("PORT", "8000"))
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
NUM_API_SERVERS = int(os.environ.get("NUM_API_SERVERS", "1"))
MAX_BATCH_SIZE = int(os.environ.get("MAX_BATCH_SIZE", "1"))
NORMALIZE = bool(os.environ.get("NORMALIZE", "0"))
DIMENSION = int(os.environ.get("DIMENSION", "256"))


class NomicTextAPI(ls.LitAPI):
    def setup(self, device: str):
        self.model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True, device=device)
        self.prefix = "search_query: "

    def decode_request(self, request):
        return self.prefix + np.asarray([request["input"]])

    def predict(self, inputs):
        embeddings = self.model.encode(inputs)
        return embeddings[:, :DIMENSION]

    def encode_response(self, output):
        return {"data": output.tolist()}

if __name__ == "__main__":
    server = ls.LitServer(
        NomicTextAPI(),
        accelerator="auto",
        max_batch_size=MAX_BATCH_SIZE,
        track_requests=True,
        workers_per_device=NUM_API_SERVERS,
        # spec=ls.OpenAIEmbeddingSpec(),
        api_path="/v1/embeddings",
    )
    server.run(
        port=PORT,
        host="0.0.0.0",
        log_level=LOG_LEVEL.lower(),
    )
