

from turtle import update
import psycopg2
import psycopg2.extras
from requests import delete

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = '12345'
port_id = 5432

conn = None
try:

    with psycopg2.connect(host= hostname,
            port = port_id,
            dbname = database,
            user = username,
            password = pwd) as conn:

        with conn.cursor(cursor_factory= psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS te_employee')

            create_script = ''' CREATE TABLE te_employee (
                                    id int PRIMARY KEY,
                                    name varchar(40) NOT NULL,
                                    salary int,
                                    dept_id varchar(30)) '''

            cur.execute(create_script)
            insert_script = 'INSERT INTO te_employee (id, name, salary, dept_id) VALUES (%s,%s,%s,%s)'
            insert_values = [(1, 'James', 12000,'D1'),(2, 'omar', 9000,'D1'),(3, 'youd', 15000,'D1')]
            for record in insert_values:
                cur.execute(insert_script,record)
            
            update_script = 'UPDATE te_employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)
            delete_script = 'DELETE FROM te_employee WHERE name = %s'
            delete_record = ('James',)
            cur.execute(delete_script, delete_record)
            cur.execute('SELECT * FROM TE_EMPLOYEE')
            for record in cur.fetchall():
                print(record['name'], record['salary'])

except Exception as error:
    print("error")

finally:
    if conn is not None:
        conn.close()

