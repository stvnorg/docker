FROM node:carbon
MAINTAINER steven.stevanus@indosystem.com
ADD . /app
WORKDIR /app/payment
RUN apt-get update
RUN apt-get install -y iputils-ping net-tools nano curl nginx iptables
RUN cp /app/default /etc/nginx/sites-enabled/default
#RUN cp /app/default.vcl /etc/varnish/default.vcl
#RUN cp /app/varnish /etc/default/varnish
#RUN echo fs.inotify.max_user_watches=582222 | tee -a /etc/sysctl.conf && sysctl -p
RUN npm install -g pm2
EXPOSE 80
#CMD service varnish start && service varnish restart && NODE_PORT=9000 pm2 start npm -- start && tail -f /etc/default/varnish
#CMD service nginx start && npm start > /dev/null 2>&1 && tail -f /var/log/nginx/access.log
CMD /app/start_app.sh
