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
