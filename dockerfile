FROM python:3.8-slim-buster

COPY requirments.txt requirments.txt

RUN pip3 install -r requirments.txt

COPY . .

CMD ["python","-m","flask","run","--host=0.0.0.0"]