FROM redis:latest
WORKDIR /db
ADD . /db
RUN apt-get update
RUN apt-get install -y iputils-ping net-tools nano curl iptables python-pip
RUN pip install redis
EXPOSE 6379
CMD ./set_redis_pass.sh

