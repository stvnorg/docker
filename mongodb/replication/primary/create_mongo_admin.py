#!/usr/bin/python

from pymongo import MongoClient

def createMongoAdmin():
	try:
		client = MongoClient('localhost:27017')
		db = client.admin
		db.add_user("mongoadmin","0711dc4c4d7365e522ff56634e8102cf5863d5aba2818c5f02615e80ed9d347b",roles=[{ 'role':'userAdminAnyDatabase', 'db':'admin'}])
	except Exception as e:
		print e

if __name__ == '__main__':
	createMongoAdmin()
