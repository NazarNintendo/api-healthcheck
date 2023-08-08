FROM python:3.10.9-slim-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src
COPY ./data.json /code/data.json

CMD ["python3", "src/main.py"]
