#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "July 2019"

import os
import gzip
import hashlib
from md5Checksum import md5Checksum

def fileRemoval(i,storage_path,cks_newdata,cur,full_fit,file):
	sql_query = 'select checksum, checksum_gz from ' + sql_list[j] + ' where file_name=%s;'
        cur.execute(sql_query, [full_fit])
	result = cur.fetchall()
	cks_db = result[0][0]
	cksgz_db = result[0][1]
	full_path = storage_path + full_fit
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
			print e
                        file.write(str(e[1]))
