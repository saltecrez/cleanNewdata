#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "March 2020"

import os
import logging
import logging.handlers

class LoggingClass(object):
    def __init__(self, logger_name='root', create_file=False):
        self.logger_name = logger_name
        self.create_file = create_file

    def get_logger(self):
        log = logging.getLogger(self.logger_name)
        log.setLevel(level=logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s','%Y-%m-%d %H:%M:%S')

        if self.create_file:
                fh = logging.FileHandler('file.log')
                fh.setLevel(level=logging.DEBUG)
                fh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setLevel(level=logging.DEBUG)
        ch.setFormatter(formatter)

        if self.create_file:
            log.addHandler(fh)

        log.addHandler(ch)
        return  log

class MissingConfParameter(Exception):
    def __init__(self, par):
        super().__init__(f"Parameter {par} not defined in configuration file")
        self.par = par
