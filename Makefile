.PHONY: test docker

docker:
	sudo docker build -t matrix_py .
	sudo docker run matrix_py

test:
	python3 tests/unit_tests.py -v

