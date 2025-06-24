build: requirements.cpu.txt
	docker build -f Dockerfile.cpu-prebaked -t mindthemath/nomic-text-1.5-api:cpu-prebaked .
	docker build -f Dockerfile.cpu -t mindthemath/nomic-text-1.5-api:cpu .

run:
	docker run --rm -ti -p 8031:8000 mindthemath/nomic-text-1.5-api:cpu-prebaked

install:
	uv sync --extra api --extra cpu

clean:
	rm -rf .venv

requirements.cpu.txt: pyproject.toml
	uv pip compile --extra cpu --extra api pyproject.toml -o requirements.cpu.txt

requirements.gpu.txt: pyproject.toml
	uv pip compile --extra cuda --extra api pyproject.toml -o requirements.gpu.txt

DOCKERFILE := Dockerfile.cpu
IMAGE      := mindthemath/nomic-text-1.5-api
TAG        := cpu-prebaked

setup-buildx:
	docker buildx create --use --name multiarch-builder
	docker buildx inspect --bootstrap

test-buildx:
	docker buildx build -f $(DOCKERFILE) \
		--platform linux/amd64,linux/arm64 \
		-t $(IMAGE):$(TAG) \
		.

push:
	docker buildx build -f $(DOCKERFILE) \
		--platform linux/amd64,linux/arm64 \
		-t $(IMAGE):$(TAG) \
		--push \
		.