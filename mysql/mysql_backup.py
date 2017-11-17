#!/usr/bin/python

import os
from datetime import datetime

ignore_tables = [
			'apilog',
			'dumpTransactions',
			'outbound_copy',
			'memberwtf',
			'member_grand',
			'member_extend_voucher',
			'member_preregister',
			'member_raptor',
			'radiuslog',
			'raptorlog',
			'tmpkasus',
			'tmpkasus2',
			'tmpkasus3',
			'tmpkasusclean',
			'tmpkasusraw',
			'tmpMapOutlet',
			'tmptransactions2016',
			'transactiondetailtmp',
			'transactionsdiff',
			'transactionstmp',
			'transactionstmp2',
			'voucher_extend',
			'voucher_raptor'
		]

def mysql_backup():
	ignore_table = [] 
	for table in ignore_tables:
		ignore_table.append("--ignore-table=memberid-live." + table)
	date = datetime.now().strftime("%Y%m%d")
	
	os.chdir("/home/deploy")
	
	try:
		command = "mysqldump -uusername -ppassword dbname " + " ".join(ignore_table) + " > /home/deploy/{}_memberid-live.sql".format(date)
		os.system(command)
	
		command = "tar -czvf {}_memberid-live.tar.gz {}_memberid-live.sql".format(date,date)
		os.system(command)

	except Exception as e:
		print e
		pass

	command = "/home/deploy/.local/bin/s3cmd --config=/home/deploy/.s3cfg put /home/deploy/{}_memberid-live.tar.gz s3://memberid-live-dump/backup/mysql/ > /home/deploy/result.txt".format(date)
	os.system(command)

	command = "rm /home/deploy/{}_memberid-live.*".format(date)
	os.system(command)

if __name__ == '__main__':
	mysql_backup()

