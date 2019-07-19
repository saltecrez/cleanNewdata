#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "July 2019"

'''
   This script is supposed to be used for the daily 
   cleaning of the ingestion folders at the telescope
   Limited to 3 instruments for now.
'''

import sys
import os
import MySQLdb
from glob import glob
from shutil import Error
from readJson import readJson
from fileRemoval import fileRemoval

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
        base = os.path.basename(os.path.splitext(os.path.normpath(i))[0])
        full_fit = base + '.fits.gz'
	ftl = base[:2]

	if ftl == instr_list[0]:
		sql = 'select id from ' + sql_list[0] + ' where file_name=%s;' 
		fileRemoval(i,sql,cur,full_fit,filelog)

	elif ftl == instr_list[1]:
		sql = 'select id from ' + sql_list[1] + ' where file_name=%s;' 
		fileRemoval(i,sql,cur,full_fit,filelog)

	elif ftl == instr_list[2]:
		sql = 'select id from ' + sql_list[2] + ' where file_name=%s;' 
		fileRemoval(i,sql,cur,full_fit,filelog)

filelog.close()
