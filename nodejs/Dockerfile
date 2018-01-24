FROM node:carbon
MAINTAINER steven.stevanus@indosystem.com
WORKDIR /app/payment
ADD . /app
RUN apt-get update
RUN apt-get install -y iputils-ping net-tools nano curl nginx iptables
RUN apt-get install -y pkg-config libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++
RUN cp /app/dev.payment.member.id.conf /etc/nginx/sites-enabled/default
RUN cp -R /app/member.id.ssl /etc/ssl/
#RUN npm install -g pm2
EXPOSE 80 443 9000
CMD /app/start_app.sh
