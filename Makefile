stencil: stencil.c
	icc -std=c99 -Ofast -xHOST -Wall $^ -o $@
	#icc -std=c99 -Ofast -xhost -qopt-report-phase=vec -qopt-report=5 -Wall $^ -o $@
