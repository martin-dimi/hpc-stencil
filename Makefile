stencil: stencil.c
	mpiicc -std=c99 -Ofast -xBROADWELL -Wall $^ -o $@

openmp: stencil_omp.c
	mpiicc -std=c99 -Ofast -xBROADWELL -qopenmp -Wall $^ -o $@

testAll:
	mkdir -p results4096
	cores=1; while [[ $$cores -le 58 ]] ; do \
		sed -i "s/srun .*/srun -n $$cores \.\/stencil 4096 4096 100/g" stencil.job ; \
		sed -i "s/output.*/output results4096\/stencil_4096_$${nodes}_$${cores}/g" stencil.job ; \
		sbatch stencil.job ; \
		((cores = cores + 1)) ; \
	done
