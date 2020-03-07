#!/usr/bin/env python

__author__ = "Elisa Londero"
__email__ = "elisa.londero@inaf.it"
__date__ = "December 2019"

from read_json import ReadJson
from glob import glob

rj = ReadJson()

class NewdataFilesList(object):
    
    def create_list(self):
        ing_fldr = rj.get_ingest_folder()
        fits_list = []
        for i in ing_fldr:
            fits_list.append(list(glob(i + '/*.fit*')))
        flat_list = [item for sublist in fits_list for item in sublist]
        return flat_list

if __name__ == "__main__":
    NewdataFilesList().create_list()
