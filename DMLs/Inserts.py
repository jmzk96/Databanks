
from DDLs.Tables import *
from psycopg2.extras import execute_values
import psycopg2

class Datainserter(DatabankCreator):

    def __init__(self):
        super().__init__()

    def insert_single_data(self,value):
        with self.connector as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("insert into table1"
                                   "(id,name,city,height)"
                                   "values (%s,%s,%s,%s);",value)
                except psycopg2.errors.IntegrityError:
                    print("Inserts NOT successful")

    def insert_many_data(self,values):
        with self.connector as conn:
            with conn.cursor() as cursor:

                try:
                    execute_values(cursor,"insert into table1"
                                          "(id,name,city,height)"
                                          "values %s;",values)
                except psycopg2.errors.IntegrityError:
                    print("Inserts NOT successful")