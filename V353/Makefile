all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 plot.py

RC.pdf: plot.py matplotlibrc header-matplotlib.tex daten/RC-Entladekurve.csv RC-Entladekurve.py | build
	TEXINPUTS=$$(pwd): python3 RC-Entladekurve.py

spannungsverhaeltnis.pdf: plot.py matplotlibrc header-matplotlib.tex daten/kondensatorspannung1.csv daten/kondensatorspannung2.csv | build
	TEXINPUTS=$$(pwd): python3 kondensatorspannung.py

phasenverschiebung.pdf: plot.py matplotlibrc header-matplotlib.tex daten/4c-1.csv daten/4c-2.csv | build
	TEXINPUTS=$$(pwd): python3 phasenverschiebung.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf

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
