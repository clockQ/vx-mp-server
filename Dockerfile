FROM python:3.8 as build

RUN mkdir -p /home/http
WORKDIR /home/http

RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
RUN pip install --no-cache-dir web.py
RUN pip install --no-cache-dir fuzzywuzzy


ENV MP_APP_ID ''
ENV MP_APP_SECRET ''

COPY . /home/http/

EXPOSE 8080
CMD ["python", "main.py", "8080"]

MAINTAINER ClockQ <zyqi@pharbers.com>
LABEL tag="mintian-mp-server" version="0.1.5" description="wechat mp server api" date="20200711"

# docker build -t clockq/mintian-mp-server:0.1.5 .
