#!/usr/bin/python

import os
from pymongo import MongoClient

def run_mongodb():
	os.system("usermod -s /bin/bash mongodb")
	os.system("touch /var/log/mongodb/mongodb.log")
	os.system("chown -R mongodb:mongodb /var/log/mongodb/mongodb.log")
	os.system("chown -R mongodb:mongodb /data/mongodb-replicaset/")
	#os.system("chown -R mongodb:mongodb /tmp/mongodb-27017.sock")

	os.system("su mongodb -c 'mongod --config /etc/mongod.conf --fork --dbpath /data/mongodb-replicaset --logpath /var/log/mongodb/mongodb.log'")
	client = MongoClient('localhost', 27017)
	db = client['admin']
	db.add_user('root', "0711dc4c4d7365e522ff56634e8102cf5863d5aba2818c5f02615e80ed9d347b", roles=[{'role':'root','db':'admin'}])
	os.system("su mongodb -c 'mongod --config /etc/mongod.conf --dbpath /data/mongodb-replicaset --shutdown'")

	os.system("su mongodb -c 'mongod --config /etc/mongod.conf --fork --dbpath /data/mongodb-replicaset --logpath /var/log/mongodb/mongodb.log'")
	client = MongoClient('localhost', 27017)
	db = client['payment']
	db.add_user('mongoadmin', "0711dc4c4d7365e522ff56634e8102cf5863d5aba2818c5f02615e80ed9d347b", roles=[{'role':'readWrite','db':'payment'}])
	os.system("su mongodb -c 'mongod --config /etc/mongod.conf --dbpath /data/mongodb-replicaset --shutdown'")
	os.system("su mongodb -c 'mongod --config /etc/mongod.conf --auth --dbpath /data/mongodb-replicaset'")

if __name__ == '__main__':
	run_mongodb()
