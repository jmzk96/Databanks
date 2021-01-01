from DDLs.Tables import *
from DMLs.Inserts import *
import time


if __name__ == '__main__':
    creator = DatabankCreator()
    creator.create_tables(with_drop=True)
    inserter = Datainserter()
    values = [(13, "Stephen F", "Mombasa", 198),
              (15, "Alex R", "Frankfurt", 150)]
    inserter.insert_many_data(values=values)
    print(os.getenv("POSTGRES_USER"))

    while True:
        print("going to sleep ...")
        time.sleep(20)
