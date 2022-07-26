# Python-and-PostgreSQL
## Installation

```bash
pip install psycopg2
```
### PostgreSQL
Connect to PostgreSQL from Python (using SQL in Python) 

:hammer: [Python to PostgreSQL](https://github.com/ELFAHIM96/Python-and-PostgreSQL/blob/main/spy2post.py)
```SQL
#db settings
#host = 'add'
#dbname = 'add db name'
#user = 'add db username'
#password = 'add db pwd'
```
```code
with psycopg2.connect(host= hostname,
            port = port_id,
            dbname = database,
            user = username,
            password = pwd) as conn:
```
###  CSV files to database PostgreSQL with Python
This part I write a code to automaticlly import CSV file to PostgreSQL database using python function
specifically be showing you how to import a CSV file to a postgres database 
[import CSV to postgreSQL](https://github.com/ELFAHIM96/Python-and-PostgreSQL/blob/main/csv2db.py)
