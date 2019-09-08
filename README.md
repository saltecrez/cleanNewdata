# cleanNewdata

Goal: clean-up newdata folder at the telescope
Targets: Asiago archive
Description: the checksum of the file in newdata on the telescope machine is compared to the checksum found in DB locally and with the checksum of the file in the local and  in the remote storages.  
Configuration parameters:
        "ingestion_folder": folder that needs to be cleaned-up
        "second_ingestion_folder": potential second folder that needs to be cleaned-up 
        "logfile": name of the logfile 
        "db_host": ip address of the host containing the local database
        "db_password": password of the local database for the user specified in db_user
        "db_user": user of the database who can access the schema specified in db_schema
        "db_schema": name of the schema to be queried
        "file_init": first two letters of the FITS files to be found in the ingestion folders eg for Asiago: ["AF","EC","SC"]
        "sql_instr": name of the instrument tables found in the metadata database eg for Asiago: ["AFO","ECH","SBI"]
        "ssh_host": ip address of the bastion between the local ingestion machine and the remote archiving machine
        "ssh_port": ssh port on bastion
        "ssh_user": username to connect to bastion
        "ssh_pwd": password to connect to bastion
        "ssh_priv_key": path to the local private key 
        "remote_host": ip address of the remote machine
        "remote_db_port": port of the database on the remote machine
        "remote_db_schema": name of the meadata schema on the remote machine
        "remote_db_user": username to connect to the database on the remote machine
        "remote_db_pwd": password to connect to the database on the remote machine
