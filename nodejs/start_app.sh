#!/bin/bash
service nginx start  
npm start > /dev/null 2>&1 & 
tail -f /var/log/nginx/access.log
