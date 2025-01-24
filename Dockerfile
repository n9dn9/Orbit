FROM python:3.11.4

WORKDIR /crudhw

COPY /. .

COPY /requirements.txt .

RUN pip install -r requirements.txt
CMD ["gunicorn", "--preload"]
