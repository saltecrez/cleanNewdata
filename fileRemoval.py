#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "July 2019"

import os
import gzip
import hashlib
from md5Checksum import md5Checksum

def fileRemoval(i,storage_path,cks_newdata,dbtable,cur,full_fit,file):
	sql_query = 'select checksum, checksum_gz from ' + dbtable + ' where file_name=%s;'
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
                        os.remove(i)
			file.write("%s %s\n" % (i, "has been removed because consistently found in database and storage"))
                except Exception as e:
                        e = sys.exc_info()
                        file.write(str(e[1]))
	else:
		file.write("%s %s\n" % (full_fit, "has been archived but the checksum cross-check among storage, newdata and database failed"))
