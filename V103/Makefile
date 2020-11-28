all: build/main.pdf

# hier Python-Skripte:
build/plot1.pdf: plot1.py matplotlibrc header-matplotlib.tex daten/*| build
	TEXINPUTS=$$(pwd): python3 plot1.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot1.pdf

# eine pdf mit allen plots
build/all-plots.pdf: build/plot1.pdf
	pdfunite \
		build/plot1.pdf \
		build/plot2.pdf \
		build/plot3.pdf \
		build/all-plots.pdf \

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
