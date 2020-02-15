From python:3

ADD src /src

RUN pip install pystrich

CMD [ "python", "./src/calculator.py" ] 


