all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot.py

build/c.pdf: c.py daten/frequenzabhaengigkeit.csv
	TEXINPUTS=$$(pwd): python c.py

build/5a.pdf: a.py daten/zeitabhaengigkeit.csv
	TEXINPUTS=$$(pwd): python a.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
#build/main.pdf: build/frequenz.pdf
build/main.pdf: build/5a.pdf build/c.pdf

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
