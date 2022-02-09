FROM python:3.8.7-slim-buster

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

RUN pip install pip==21.2.4 && \
    pip install -r requirements.txt

CMD ["python", "app/main.py"]