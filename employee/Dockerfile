FROM ubuntu:latest
WORKDIR /app

COPY requirements.txt /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y libmysqlclient-dev pkg-config && \
    pip install -r requirements.txt

COPY . /app

CMD [ "python3" , "manage.py" , "runserver" , "0.0.0.0:8000" ]

