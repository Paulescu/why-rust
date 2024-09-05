time-python:
	cd sum-in-python && \
	time poetry run python src/sum_up_to.py ${N}

time-python-with-numpy:
	cd sum-in-python && \
	time poetry run python src/sum_up_to.py ${N} --numpy

time-rust:
	cd sum-in-rust && \
	cargo build --release && \
	time ./target/release/sum-in-rust --number ${N}


sums:
	@echo "**********************************"
	@echo "Python:"
	@make time-python N=${N}
	
	@echo "**********************************"
	@echo "Python with Numpy:"
	@make time-python-with-numpy N=${N}

	@echo "**********************************"
	@echo "Rust:"
	@make time-rust N=${N}
