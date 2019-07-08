#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "July 2019"

'''
   This script is supposed to be used for the daily 
   cleaning of the ingestion LBT folder on the mountain
'''

import time
import sys
import os
import shutil
import MySQLdb
from glob import glob
from shutil import Error
from readJson import readJson
from fileRemoval import fileRemoval

# Load input file 
CWD = os.getcwd()
cnf = readJson('config.json',CWD)

# Open logfile 
filelog = open(cnf['logfile'],'a')

# create files list
a = list(glob(cnf['ingestion_folder'] + '/*.fit*'))

# connect to DB
db = MySQLdb.connect(cnf['db_host'],cnf['db_user'],cnf['db_password'],cnf['db_schema']) 
cur = db.cursor()

# remove files after cecking DB
for i in a:
        base = os.path.basename(os.path.splitext(os.path.normpath(i))[0])
        full_fit = base+'.fits.gz'
	ftl = base[:3]

	if ftl == 'luc':
		sql = cnf['sql_luci']
		try:
			fileRemoval(i,sql,cur,full_fit,filelog)
		except Exception as e:
			e = sys.exc_info()
			filelog.write(str(e[1]))
	
	elif ftl == 'mod':
                sql = cnf['sql_mods']
                try:
                        fileRemoval(i,sql,cur,full_fit,filelog)
                except Exception as e:
                        e = sys.exc_info()
                        filelog.write(str(e[1]))

	elif ftl == 'lbc':
                sql = cnf['sql_lbc']
                try:
                        fileRemoval(i,sql,cur,full_fit,filelog)
                except Exception as e:
                        e = sys.exc_info()
                        filelog.write(str(e[1]))

filelog.close()