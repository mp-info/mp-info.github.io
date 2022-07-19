clean:
	jupyter-book clean files

build: clean
	jupyter-book build files

run: build
	python3 -m http.server --directory files/_build/html 8000
