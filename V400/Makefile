all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot.py

build/1.pdf: 1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python 1.py

build/2.pdf: 2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python 2.py

build/4.pdf: 4.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python 4.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
#build/main.pdf: build/plot.pdf
build/main.pdf: build/1.pdf
build/main.pdf: build/2.pdf
build/main.pdf: build/4.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
