FROM ubuntu:latest

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "./main.py", "usr/local", "https://jisho.org/", "https://www.tokyodev.com/"]