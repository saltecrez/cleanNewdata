#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "August 2019"

def storagePathConstructor(cur,file_version,dbtable,filename):
	sql_query = 'select storage_path, file_path from ' + dbtable + ' where file_name=%s and file_version=%s;'
        cur.execute(sql_query, [filename,file_version])
        result_query = cur.fetchall()
        storage_path = result_query[0][0]
        file_path = result_query[0][1]
        full_path = storage_path + file_path + '/' + str(file_version) + '/' 
	return full_path
