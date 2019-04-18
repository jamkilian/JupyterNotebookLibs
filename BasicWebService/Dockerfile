from alpine:latest

WORKDIR /app

COPY . /app

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip \
    && pip3 --no-cache-dir install -r requirements.txt

EXPOSE 8080

CMD ["python3", "BasicWebService.py"]