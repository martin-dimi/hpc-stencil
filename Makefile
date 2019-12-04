stencil: stencil.c
	mpiicc -std=c99 -Ofast -xBROADWELL -Wall $^ -o $@

testAll:
	mkdir -p results1024
	cores=1; while [[ $$cores -le 58 ]] ; do \
		sed -i "s/srun .*/srun -n $$cores \.\/stencil 1024 1024 100/g" stencil.job ; \
		sed -i "s/output.*/output results1024\/stencil_1024_$${nodes}_$${cores}/g" stencil.job ; \
		sbatch stencil.job ; \
		((cores = cores + 1)) ; \
	done
