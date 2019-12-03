stencil: stencil.c
	mpiicc -std=c99 -Ofast -xBROADWELL -Wall $^ -o $@

testAll:
	mkdir -p results8000
	nodes=1 ; while [[ $$nodes -le 2 ]] ; do \
		cores=1; while [[ $$cores -le 28 ]] ; do \
			sed -i "s/nodes\s[0-9]\+/nodes $$nodes/g" stencil.job ; \
			sed -i "s/ntasks\-per\-node\s[0-9]\+/ntasks\-per\-node $$cores/g" stencil.job ; \
			sed -i "s/output.*/output results8000\/stencil_8000_$${nodes}_$${cores}/g" stencil.job ; \
			sbatch stencil.job ; \
			((cores = cores + 1)) ; \
		done ; \
		((nodes = nodes + 1)) ; \
	done
