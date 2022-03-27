FROM alpine:latest

RUN apk add py3-pip python3

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD ["python3","app.py"]