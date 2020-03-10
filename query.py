#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "March 2020"

import os
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper
from logging_class import LoggingClass
from database import MySQLDatabase

log = LoggingClass('',True).get_logger()

def db_query(tab, session, fname):
    metadata = MetaData()
    table_name = tab
    table_object = Table(table_name, metadata,
        Column('id', Integer, primary_key=True),
        Column('file_name', String(255)),
        Column('storage_path', String(255)),
        Column('file_path', String(255)),
        Column('file_version', Integer()),
        Column('checksum', String(255)),
        Column('checksum_gz', String(255)))

    class TableObject(object):
         pass

    try:
        mapper(TableObject, table_object)
        rows = session.query(TableObject)
        flt = rows.filter(TableObject.file_name == fname)
        for j in flt:
            if j.file_name:
                path = j.storage_path + j.file_path
                full_path = os.path.join(path,str(j.file_version),j.file_name)
                return full_path, j.checksum, j.checksum_gz
    except Exception as e:
            log.error("{0}".format(e))
    
if __name__ == "__main__":
    user = 'archa'
    pwd = 'Archa123.'
    host = 'localhost'
    dbname = 'metadata_asiago'
    port = '3307'
    db = MySQLDatabase(user,pwd,host,port,dbname)
    Session = db.create_session()
    print(db_query('AFO',Session,'AF597076.fits.gz'))
