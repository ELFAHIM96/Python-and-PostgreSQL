import os
import numpy as np
import pandas as pd
import psycopg2


from csv2db import *

#settings
dataset_dir = ''

#db settings
#host = 'add'
#dbname = 'add db name'
#user = 'add db username'
#password = 'add db pwd'
host = 'localhost'
dbname = 'demo'
user = 'postgres'
password= ''
port_id = 5432
#configure environment and create main df
csv_files = csv_files()
configure_dataset_directory(csv_files, dataset_dir)
df = create_df(dataset_dir, csv_files)

for k in csv_files:

    #call dataframe
    dataframe = df[k]

    #clean table name
    tbl_name = clean_tbl_name(k)
    
    #clean column names
    col_str, dataframe.columns = clean_colname(dataframe)
    
    #upload data to db   
    upload_to_db(host, 
                 dbname, 
                 user, 
                 password, 
                 tbl_name, 
                 col_str, 
                 file=k, 
                 dataframe=dataframe, 
                 dataframe_columns=dataframe.columns)