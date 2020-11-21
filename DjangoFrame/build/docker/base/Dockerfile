FROM ubuntu:16.04
FROM python:3.6


ENV http_proxy=http://xxx.xxx.xxx.xxx:3128
ENV https_proxy=http://xxx.xxx.xxx.xxx:3128

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y \
    vim \
	git \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
        nodejs \
        npm \
        default-libmysqlclient-dev && \
        pip3 install --upgrade -i https://pypi.doubanio.com/simple/ pip setuptools && \
  	rm -rf /var/lib/apt/lists/*

RUN pip3 install -i https://pypi.doubanio.com/simple/ uwsgi

COPY requirements.txt /data/Project/
RUN pip3 install -i https://pypi.doubanio.com/simple/ -r /data/Project/requirements.txt

COPY ./build/nginx/nginx.conf /etc/nginx/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY ./build/nginx/conf.d  /etc/nginx/conf.d

ENV PYTHONIOENCODING=utf-8

EXPOSE 9990 9999
