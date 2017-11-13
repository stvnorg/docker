FROM ubuntu:latest
MAINTAINER steven.stevanus@indosystem.com
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list
RUN apt-get update
RUN apt-get install -y python python-setuptools python-dev python-pip
RUN apt-get install -y mongodb-org
RUN pip install pymongo
RUN mkdir -p /data/db
EXPOSE 27017
WORKDIR /db
ADD . /db
CMD ["mongod --auth"]
CMD ["/db/create_mongo_admin.py"]
