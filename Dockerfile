From python:3

ADD src /src

RUN pip install pystich

CMD [ "python", "./src/calculator.py" ] 


