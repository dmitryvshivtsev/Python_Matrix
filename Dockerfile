FROM python:3.10

RUN mkdir -p /usr/src/py_matrix/
COPY . /usr/src/py_matrix/
WORKDIR /usr/src/py_matrix/tests/

CMD ["python3", "unit_tests.py"]
