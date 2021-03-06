#!/usr/bin/python

import os
from pymongo import MongoClient

def run_mongodb():
	os.system("usermod -s /bin/bash mongodb")
	os.system("touch /var/log/mongodb/mongod.log")
	os.system("chown -R mongodb:mongodb /var/log/mongodb/mongodb.log")
	os.system("chown -R mongodb:mongodb /data/mongodb")
	#os.system("chown -R mongodb:mongodb /tmp/mongodb-27017.sock")

	os.system("su mongodb -c 'mongod --replSet rs0 --fork --dbpath /data/mongodb --logpath /var/log/mongodb/mongodb.log'")
	client = MongoClient('localhost', 27017)
	config = {'_id': 'rs0', 'members': [{'_id': 0, 'host': 'localhost:27017'}]}
	client.admin.command('replSetInitiate', config)
	os.system("su mongodb -c 'mongod --dbpath /data/mongodb --shutdown'")

	os.system("su mongodb -c 'mongod --fork --dbpath /data/mongodb --logpath /var/log/mongodb/mongodb.log'")
	client = MongoClient('localhost', 27017)
	db = client['admin']
	db.add_user('root', "0711dc4c4d7365e522ff56634e8102cf5863d5aba2818c5f02615e80ed9d347b", roles=[{'role':'root','db':'admin'}])
	os.system("su mongodb -c 'mongod --dbpath /data/mongodb --shutdown'")

	os.system("su mongodb -c 'mongod --fork --dbpath /data/mongodb --logpath /var/log/mongodb/mongodb.log'")
	client = MongoClient('localhost', 27017)
	db = client['payment']
	db.add_user('mongoadmin', "0711dc4c4d7365e522ff56634e8102cf5863d5aba2818c5f02615e80ed9d347b", roles=[{'role':'readWrite','db':'payment'}])
	os.system("su mongodb -c 'mongod --dbpath /data/mongodb --shutdown'")
	os.system("su mongodb -c 'mongod --replSet rs0 --dbpath /data/mongodb --logpath /var/log/mongodb/mongodb.log --auth'")

	#config = {'_id': 'rs0', 'members': [
	#	{'_id': 0, 'host': 'localhost:27017'}]}
	#db.admin.command('replSetInitiate', config)

if __name__ == '__main__':
	run_mongodb()
