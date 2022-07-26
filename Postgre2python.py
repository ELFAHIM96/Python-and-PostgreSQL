
import psycopg2

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = '12345'
port_id = 5432

conn = None
cur = None


conn = psycopg2.connect(host= hostname,
    port = port_id,
    dbname = database,
    user = username,
    password = pwd)

cur = conn.cursor()

create_script = ''' CREATE TABLE T_employee (
                        id int PRIMARY KEY,
                        name varchar(40) NOT NULL,
                        salary int,
                        dept_id varchar(30)) '''  

cur.execute(create_script)
insert_script = 'INSERT INTO T_employee (id, name, salary, dept_id) VALUES (%s,%s,%s,%s)'
insert_value = (1, 'James', 12000,'D1')
cur.execute(insert_script,insert_value)
conn.commit()
