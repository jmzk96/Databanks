import psycopg2
from dotenv import load_dotenv
import os

load_dotenv("database.env") #Name von .env Datei muss spezifiziert werden
user = os.getenv("POSTGRES_USER")
dbname = os.getenv("POSTGRES_DB")
password = os.getenv("POSTGRES_PASSWORD")
port = os.getenv("POSTGRES_PORT")
host =os.getenv("POSTGRES_HOST")

class DatabankCreator:

    def __init__(self):
        self.connector =psycopg2.connect(host =host,user=user,dbname=dbname,password=password,port=port)

    def create_tables(self,with_drop:bool=True):
        with self.connector as conn:
            with conn.cursor() as cursor:
                if with_drop:
                    cursor.execute("drop table if exists table1 cascade;")
                try:
                    cursor.execute("create table table1("
                                   "id int,"
                                   "name varchar(50),"
                                   "city varchar(30),"
                                   "height int,"
                                   "primary key(id,name)"
                                   ");")

                except psycopg2.errors.DuplicateTable as dt:
                    print("Database/Table already exists")
                else:
                    print("Table successfully created")



    def close_connector(self):
        self.connector.close()