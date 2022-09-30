all: build/plot.pdf build/exp.pdf

build/plot.pdf: plot.py | build
	python plot.py

build/exp.pdf: exp.py | build
	python exp.py

clean: 
	rm -rf build

build: 
	mkdir -p build

.PHONY: build clean

