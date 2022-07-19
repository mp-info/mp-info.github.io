clean:
	poetry run jupyter-book clean files

build: clean
	poetry run jupyter-book build files/

run: build
	poetry run python3 -m http.server --directory files/_build/html 8000