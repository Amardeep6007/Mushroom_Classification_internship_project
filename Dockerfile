# FROM python:3.7-slim-buster

# RUN apt update -y && apt install awscli -y
# WORKDIR /app

# COPY ./app
# RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]

FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app