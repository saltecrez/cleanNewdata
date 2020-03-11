#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "September 2019"

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logging_class import LoggingClass

log = LoggingClass('',True).get_logger()

class MySQLDatabase(object):
    def __init__(self, user, pwd, host, port, dbname):
        self.user = user
        self.pwd = pwd
        self.host = host
        self.port = port
        self.dbname = dbname

    def create_session(self):
        sdb = 'mysql+pymysql://%s:%s@%s:%s/%s'%(self.user,self.pwd,self.host,self.port,self.dbname)
        try:
            engine = create_engine(sdb)
            db_session = sessionmaker(bind=engine)
            return db_session()
        except Exception as e:
            msg = "Database session creation excep - MySQLDatabase.create_session -- "
            log.error("{0}{1}".format(msg,e))

    def validate_session(self):
        try:
            connection = self.create_session().connection()
            return True
        except Exception as e:
            msg = "Database session validation excep - MySQLDatabase.validate_session -- "
            log.error("{0}{1}".format(msg,e))
            return False

    def close_session(self):
        try:
            self.create_session().close()
            return True
        except Exception as e: 
            msg = "Database session closing excep - MySQLDatabase.close_session -- "
            log.error("{0}{1}".format(msg,e))
            return False

if __name__ == "__main__":
    user = 'archa'
    pwd = 'Arch123.'
    host = 'localhost'
    dbname = 'metadata_asiago'
    port = '3307'
    db = MySQLDatabase(user,pwd,host,port,dbname)
    Session = db.create_session()
    db.validate_session()
    print(db.close_session())
