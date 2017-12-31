FROM python:3.6-alpine

ENV APP_DIR /app
EXPOSE 5000

RUN apk update && \
    apk upgrade && \
    apk add -uU bash \
                nano \
                gcc \
                openssh \
                openssl \
                openssl-dev \
                linux-headers \
                musl-dev \
                libffi \
                libffi-dev && \
    mkdir ${APP_DIR}

WORKDIR ${APP_DIR}

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

COPY ./app ${APP_DIR}

ENTRYPOINT ["python3", "app.py"]
