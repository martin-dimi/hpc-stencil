stencil: stencil.c
	mpiicc -std=c99 -Ofast -xBROADWELL -Wall $^ -o $@
