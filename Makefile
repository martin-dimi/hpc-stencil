stencil: stencil.c
	mpiicc -std=c99 -Ofast -xBROADWELL -Wall $^ -o $@

testAll:
	mkdir -p results8000
	cores=1; while [[ $$cores -le 58 ]] ; do \
		sed -i "s/srun .*/srun -n $$cores \.\/stencil 8000 8000 100/g" stencil.job ; \
		sed -i "s/output.*/output results8000\/stencil_8000_$${nodes}_$${cores}/g" stencil.job ; \
		sbatch stencil.job ; \
		((cores = cores + 1)) ; \
	done
