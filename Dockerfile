# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /objective-function-service

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt 

COPY . .

ENTRYPOINT [ "python" ]

CMD ["app.py" ]