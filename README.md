# cleanNewdata

- **Goal**: clean-up newdata folder on the ingestion machine 

- **Targets**: all the archives - to be installed on the first ingestion node
  
- **Description**: the checksum of the file in newdata on the ingestion machine is compared to the checksum found in DB and with the checksum of the file in the storage. If the checksums match, the file is removed. All these operations are performed locally, at the ingestion site. Remember that in ordero to guarantee file integrity an additional check must be done at the final archiving site.   
 
- **Configuration parameters**:

      "ingest_folder": folders that need to be cleaned-up  
      "db_host": ip address of the host containing the local database  
      "db_pwd": local database password
      "db_user": local database user 
      "db_name": local database to be queried
      "db_port": local database port
      "email": 
      "sender":
      "smtp_host":
      "db_tables":
