stencil: stencil.c
	icc -std=c99 -Ofast -xHOST -Wall $^ -o $@
