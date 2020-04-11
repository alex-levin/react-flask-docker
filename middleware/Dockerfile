FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY api.py requirements.txt /usr/src/app/

RUN pip3 install -r requirements.txt

ENV FLASK_APP=api.py
ENV FLASK_DEBUG=1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

# CMD ["python3", "api.py"]
