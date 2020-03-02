uthor__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "June 2018"

from util import VerifyLinux
from read_json import ReadJson
from database import MySQLDatabase

def main():
    VerifyLinux()

    rj = ReadJson()

    dbuser = rj.get_db_user()   
    dbpwd = rj.get_db_pwd()   
    dbhost = rj.get_db_host()   
    dbname = rj.get_db_name()   

    db = MySQLDatabase(dbuser, dbpwd, dbhost, dbname)
    Session = db.create_session()


if __name__ == "__main__":
   main()
