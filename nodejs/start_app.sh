#!/bin/bash
service nginx start
npm install
#NODE_ENV=development pm2 start src/index.js npm -- start -i 1 -x -- --port 9000 -i 1
npm start > /app/logs.txt &
#npm start > /dev/null 2>&1 & 
#pm2 start npm -- start
tail -f /var/log/nginx/access.log
