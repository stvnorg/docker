FROM ubuntu:latest
MAINTAINER steven.stevanus@indosystem.com
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list
RUN apt-get update
RUN apt-get install -y mongodb-org
RUN apt-get install -y iputils-ping nano net-tools
RUN apt-get install -y python python-pip
RUN pip install pymongo
WORKDIR /db
ADD . /db
#RUN cp /db/mongod.conf /etc/mongod.conf
EXPOSE 27017
CMD /db/run_mongodb.py
