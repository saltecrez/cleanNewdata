#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "June 2018"

import os
import json

class ReadJson(object):
    def _create_dictionary(self):
        json_config_file_path = '%s/%s' % (os.getcwd(), 'conf.json')
        config_properties = {}
        with open(json_config_file_path) as data_file:
            config_properties = json.load(data_file)
        return config_properties

    def get_recipient(self):
        recipient = self._create_dictionary().get("email")
        return recipient

    def get_sender(self):
        sender = self._create_dictionary().get("sender")
        return sender

    def get_smtp_host(self):
        smtp_host = self._create_dictionary().get("smtphost")
        return smtp_host

    def get_db_host(self):
        db_host = self._create_dictionary().get("dbhost")
        return db_host

    def get_db_user(self):
        db_user = self._create_dictionary().get("dbuser")
        return db_user

    def get_db_pwd(self):
        db_pwd = self._create_dictionary().get("dbpwd")
        return db_pwd

    def get_db_name(self):
        db_name = self._create_dictionary().get("dbname")
        return db_name

    def get_db_port(self):
        db_port = self._create_dictionary().get("dbport")
        return db_port

    def get_db_tables(self):
        db_tables = self._create_dictionary().get("dbtables")
        return db_tables

    def get_ingest_folder(self):
        ing_folder = self._create_dictionary().get("ingestfolder")
        return ing_folder

if __name__ == "__main__":
    filename = 'conf.json'
    print(ReadJson().get_db_pwd())
