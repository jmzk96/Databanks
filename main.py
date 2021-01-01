from DDLs.Tables import *
from DMLs.Inserts import *
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv(dotenv_path="database.env")
    creator = DatabankCreator()
    creator.create_tables(with_drop=True)
    inserter = Datainserter()
    values =[(13,"Stephen F","Mombasa",198),(15,"Alex R","Frankfurt",150)]
    inserter.insert_many_data(values=values)
    print(os.getenv("POSTGRES_USER"))




