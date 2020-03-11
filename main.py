#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "June 2018"

import os
from glob import glob
from query import db_query
from utilities import md5Checksum
from logging_class import LoggingClass
from read_json import ReadJson
from database import MySQLDatabase
from logging_class import MissingConfParameter

rj = ReadJson()
log = LoggingClass('',True).get_logger()

class NewdataFilesList(object):

    def create_list(self):
        try:
            ing_fldr = rj.get_ingest_folder()
            fits_list = []
            for i in ing_fldr:
                fits_list.append(list(glob(i + '/*.fit*')))
            flat_list = [item for sublist in fits_list for item in sublist]
            return flat_list
        except Exception as e:
            msg = "Newdata files list excep - NewdataFilesList.create_list -- "
            log.error("{0}{1}".format(msg,e))

def main():
    dbuser = rj.get_db_user();  dbpwd = rj.get_db_pwd()   
    dbhost = rj.get_db_host();  dbname = rj.get_db_name()   
    dbport = rj.get_db_port();  dbtables = rj.get_db_tables()

    db = MySQLDatabase(dbuser, dbpwd, dbhost, dbport, dbname)

    try:
        Session = db.create_session()
    
        files_list = NewdataFilesList().create_list()
    
        for file_path in files_list:
            cks_newdata = md5Checksum(file_path).calculate_checksum()
            fname = os.path.basename(os.path.splitext(os.path.normpath(file_path))[0])
            fname_gz = fname + '.fits.gz' 
    
            for tbl in dbtables:
                db_element = db_query(tbl, Session, fname_gz) 
    
                if db_element is not None:
                    storage_path = db_element[0]
                    cks_db = db_element[1]
                    cksgz_db = db_element[2]
                    cksgz_stg = md5Checksum(storage_path).calculate_checksum() 
                    cks_stg = md5Checksum(storage_path).get_checksum_gz()
    
                    if cksgz_stg == cksgz_db and cks_stg == cks_db == cks_newdata:
                        try:
                            os.remove(file_path)
                        except Exception as e:
                            msg = "File removal exception --"
                            log.error("{0}{1}".format(msg,e))  	
    except Exception as e:
        log.error("{0}".format(e))
    finally:
        db.close_session()

if __name__ == "__main__":
   main()
