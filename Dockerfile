From python:3

ADD src /src

RUN pip install pystrich

CMD [ "python",  "./src/test_CsvReader.py"]


