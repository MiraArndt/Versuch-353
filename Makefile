all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot.py
build/plot2.pdf: plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot2.py
build/plot3.pdf: plot3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot3.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf
build/main.pdf: build/plot2.pdf
build/main.pdf: build/plot3.pdf


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
