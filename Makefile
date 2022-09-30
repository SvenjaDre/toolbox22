all: build/plot.pdf

build/plot.pdf: plot.py | build
	python plot.py

clean: 
	rm -rf build

build: 
	mkdir -p build

.PHONY: build clean
