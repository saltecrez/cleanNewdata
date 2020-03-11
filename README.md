# cleanNewdata

- **Goal**: clean-up newdata folder on the ingestion machine 

- **Targets**: all the archives - to be installed on the ingestion node (where also fitsImporter and preProcessor are active)
  
- **Description**: the checksum of the file in newdata on the ingestion machine is compared to the checksum found in DB and with the checksum of the file in the storage. If the checksums match, the file is removed. All these operations are performed locally, at the ingestion site. Remember that in order to guarantee file integrity an additional check must be done at the final archiving site.   
 
- **Configuration parameters**:

      "ingest_folder": list of folders that need to be cleaned-up  
      "db_host": ip address of the host containing the local database  
      "db_pwd": local database password
      "db_user": local database user 
      "db_name": local database to be queried
      "db_port": local database port
      "email": email receiving the alerts 
      "sender": email sender
      "smtp_host": smtp domain of the local machine sending the email
      "db_tables": list of tables inside db_name that need to be queried

- **Requirements**:
    - python3
    - pip install astropy
    - pip install sqlalchemy
    - pip install pymysql

- **Usage**:
    - configure the conf.json file
    - /usr/bin/python main.py 
