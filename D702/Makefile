all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot.py

build/vanadium.pdf: daten/vanadium.csv
build/vanadium.pdf: vanadium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python vanadium.py

build/rhodium.pdf: daten/rhodium.csv
build/rhodium.pdf: rhodium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 rhodium.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf build/vanadium.pdf build/rhodium.pdf content/auswertung.tex

build/main.pdf: build/rhodium.pdf

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
