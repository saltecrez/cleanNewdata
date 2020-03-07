#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "June 2018"

import os
from query import db_query
from util import md5Checksum
from util import VerifyLinux
from read_json import ReadJson
from database import MySQLDatabase
from newdata_list import NewdataFilesList

def main():
    VerifyLinux()

    rj = ReadJson()

    dbuser = rj.get_db_user();  dbpwd = rj.get_db_pwd()   
    dbhost = rj.get_db_host();  dbname = rj.get_db_name()   
    dbport = rj.get_db_port();  dbtables = rj.get_db_tables()

    db = MySQLDatabase(dbuser, dbpwd, dbhost, dbport, dbname)
    Session = db.create_session()

    files_list = NewdataFilesList().create_list()

    for file_path in files_list:
         chksm_newdata = md5Checksum(file_path).calculate_checksum()
         fname = os.path.basename(os.path.splitext(os.path.normpath(file_path))[0])
         fname_gz = fname + '.fits.gz' 
         for tbl in dbtables:
             db_elements = db_query(tbl, Session, fname_gz) 
             if db_elements is not None:
                 storage_path = db_elements[0]
                 chks_db = db_elements[1]
                 chksgz_db = db_elements[2]

if __name__ == "__main__":
   main()
