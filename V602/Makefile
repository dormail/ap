all: build/main.pdf

# hier Python-Skripte:
build/bragg.pdf:  plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 plot.py 
build/spektrum.pdf: spektrum.py  matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 spektrum.py
build/Brom.pdf: abspektrum.py  matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 abspektrum.py 
build/Gallium.pdf: abspektrum.py  matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 abspektrum.py
build/Rubidium.pdf: abspektrum.py  matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 abspektrum.py
build/Strontium.pdf: abspektrum.py  matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 abspektrum.py
build/Zink.pdf: abspektrum.py  matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python3 abspektrum.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/bragg.pdf
build/main.pdf: build/spektrum.pdf
build/main.pdf: build/Brom.pdf
build/main.pdf: build/Gallium.pdf
build/main.pdf: build/Rubidium.pdf
build/main.pdf: build/Strontium.pdf
build/main.pdf: build/Zink.pdf

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
