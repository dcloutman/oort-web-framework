# syntax=docker/dockerfile:1

# To build, run 
#
#    ```
#    docker build -t kuiper-test-web-portal -f ../../docker/www
#    ```
# from ../../www/

FROM python:3.10.5-alpine
WORKDIR /app
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=127.0.0.1
COPY ../requirements.txt requirements.txt
RUN apk add --no-cache gcc musl-dev linux-headers; \
    apk add bash; \
    apk add doas; \
    adduser -H -D -s /bin/bash -g "app" app; \
    apk add g++; \
    apk add imagemagick; \
    python -m pip install --upgrade pip; \
    python -m pip install -U wheel setuptools; \
    python setup.py sdist bdist_wheel; \
    pip install -r /app/requirements.txt
EXPOSE 5150
COPY .. .
CMD ["flask", "run"]
