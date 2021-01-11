all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 plot.py

build/4a.pdf: matplotlibrc header-matplotlib.tex daten/RC-Entladekurve.csv RC-Entladekurve.py | build
	TEXINPUTS=$$(pwd): python3 RC-Entladekurve.py

build/4b.pdf: matplotlibrc header-matplotlib.tex daten/kondensatorspannung1.csv daten/kondensatorspannung2.csv kondensatorspannung.py | build
	TEXINPUTS=$$(pwd): python3 kondensatorspannung.py

build/4c.pdf: matplotlibrc header-matplotlib.tex daten/4c-1.csv daten/4c-2.csv phasenverschiebung.py | build
	TEXINPUTS=$$(pwd): python3 phasenverschiebung.py

build/polarplot.pdf: matplotlibrc header-matplotlib.tex polarplot.py | build
	TEXINPUTS=$$(pwd): python3 polarplot.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/4a.pdf build/4b.pdf build/4c.pdf build/polarplot.pdf

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

build/all-plots.pdf: build/4a.pdf build/4b.pdf build/4c.pdf
	pdfunite \
		build/4a.pdf build/4b.pdf build/4c.pdf \
		build/all-plots.pdf

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
