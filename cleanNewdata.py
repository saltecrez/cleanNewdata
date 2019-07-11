#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "July 2019"

'''
   This script is supposed to be used for the daily 
   cleaning of the ingestion LBT folder on the mountain
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
		fileRemoval(i,sql,cur,full_fit,filelog)

	elif ftl == 'mod':
                sql = cnf['sql_mods']
		fileRemoval(i,sql,cur,full_fit,filelog)

	elif ftl == 'lbc':
                sql = cnf['sql_lbc']
		fileRemoval(i,sql,cur,full_fit,filelog)

filelog.close()
