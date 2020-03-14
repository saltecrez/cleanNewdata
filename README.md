# cleanNewdata

- **Goal**: clean-up newdata folder on the ingestion machine 

- **Targets**: all the archives - to be installed on the ingestion node (where also fitsImporter and preProcessor are active)
  
- **Description**: the checksum of the file in newdata on the ingestion machine is compared to the checksum found in DB and with the checksum of the file in the storage. If the checksums match, the file is removed. All these operations are performed locally, at the ingestion site. Remember that in order to guarantee file integrity an additional check must be done at the final archiving site. This tool DOES NOT ensure that kind of integrity.   
 
- **Configuration parameters**:

      -ingest_folder [string]: list of folders that need to be cleaned-up  
      -db_host [string]: IP address/name of the host containing the local database (usually localhost) 
      -db_pwd [string]: local database password
      -db_user [string]: local database user 
      -db_name [string]: name of the local database to be queried
      -db_port [unsigned long]: local database port
      -email [string]: email receiving the alerts 
      -sender [string]: email sender
      -smtp_host [string]: smtp domain of the local machine sending the email
      -db_tables [string vector]: list of tables inside db_name that need to be queried

- **Requirements**:
    - python3
    - pip3 --user install astropy
    - pip3 --user install sqlalchemy
    - pip3 --user install pymysql

- **Usage**:
    - configure the conf.json file
    - /usr/bin/python3 main.py 
