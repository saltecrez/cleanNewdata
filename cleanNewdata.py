#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "July 2019"

'''
   This script is supposed to be used for the daily 
   cleaning of the ingestion folders at the telescope
'''

import sys
import os
import MySQLdb
from glob import glob
from readJson import readJson
from fileRemoval import fileRemoval
from md5Checksum import md5Checksum
from storagePathConstructor import storagePathConstructor

# Get current working directory
CWD = os.path.dirname(os.path.abspath(sys.argv[0]))

# Load input file 
cnf = readJson('config.json',CWD)

# Open logfile 
filelog = open(CWD + '/' + cnf['logfile'],'a')

# create files list
a = list(glob(cnf['ingestion_folder'] + '/*.fit*'))
b = list(glob(cnf['second_ingestion_folder'] + '/*.fit*'))
files_list = a + b

# connect to DB
db = MySQLdb.connect(cnf['db_host'],cnf['db_user'],cnf['db_password'],cnf['db_schema']) 
cur = db.cursor()

# instruments list
instr_list = cnf['file_init'] 
sql_list = cnf['sql_instr'] 

# remove files after cecking DB
for i in files_list:
	cks_newdata = md5Checksum(i)
        base = os.path.basename(os.path.splitext(os.path.normpath(i))[0])
        full_fit = base + '.fits.gz'
	ftl = base[:2]

	for j in range(len(instr_list)):
		if ftl == instr_list[j]:
			sql_query = 'select id from ' + sql_list[j] + ' where file_name=%s;' 
			cur.execute(sql_query, [full_fit])
			if cur.rowcount == 1:
				try:
					storage_path = storagePathConstructor(cur,sql_list[j],full_fit)
					fileRemoval(i,storage_path,cks_newdata,cur,full_fit,filelog)
				except Exception as e:
					e = sys.exc_info()
					print e
					filelog.write(str(e[1]))
			break
		else:
			continue

filelog.close()
