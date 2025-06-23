build: requirements.cpu.txt
	docker build -f Dockerfile.cpu -t mindthemath/embed-text-litserve:cpu .

run:
	docker run --rm -ti -p 8031:8000 mindthemath/embed-text-litserve:cpu 

install:
	uv sync --extra api --extra cpu

clean:
	rm -rf .venv

requirements.cpu.txt: pyproject.toml
	uv pip compile --extra cpu --extra api pyproject.toml -o requirements.cpu.txt
