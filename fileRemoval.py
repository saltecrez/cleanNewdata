#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "July 2019"

import os
import gzip
import hashlib
from md5Checksum import md5Checksum

def fileRemoval(i,sql_query,cks_newdata,cur,full_fit,file):
        cur.execute(sql_query, [full_fit])
	result = cur.fetchall()
	id_db = result[0][0]
	cks_db = result[0][1]
	cksgz_db = result[0][2]
	stpath = result[0][3]
	flpath = result[0][4]
	flver = result[0][5]
	full_path = stpath + flpath + '/' + str(flver) + '/' + full_fit
	cksgz_storage = md5Checksum(full_path)

        fit = gzip.open(full_path, 'rb')
        fit_content = fit.read()
	cks_storage = hashlib.md5(fit_content).hexdigest()
        fit.close()

        if cksgz_storage == cksgz_db and cks_storage == cks_db == cks_newdata:
		try:
			file.write(i + '\n')
                        os.remove(i)
                except Exception as e:
                        e = sys.exc_info()
                        file.write(str(e[1]))
