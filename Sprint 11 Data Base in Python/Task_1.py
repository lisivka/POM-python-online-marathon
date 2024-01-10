# Create a Python program to use the sqlite database named "q1.db".
# The query to the database should display information,
# as shown in the example below, including phrases: about the successful connection,
# the total number of records, the actual records, the record of closing the database.
# From the table of "customers" to deduce all records
# for which in a "grade" field of value more than 200 with sort ordering on id
#
#
#
# For example output:
#
# Connected to SQLite
# Total rows are:   2
# Printing each row
# Id:  3022
# Name:  Nik Rimando
# City:  Madrid
# Grade:  1000
# Seller:  6001
#
#
# Id:  3025
# Name:  Grem Zusisa
# City:  USA
# Grade:  2000
# Seller:  6002
#
#
# The SQLite connection is closed

import sqlite3

def parse_data(data: list):
    print(f"Total rows are:   {len(data)}")
    print("Printing each row")
    for row  in data:
        print(f"Id:  {row[0]}")
        print(f"Name:  {row[1]}")
        print(f"City:  {row[2]}")
        print(f"Grade:  {row[3]}")
        print(f"Seller:  {row[4]}")
        print("\n")

def get_all_data(name_table="my_table", request_sql=None) -> tuple:
    if request_sql is None:
        request_sql = f"SELECT * FROM {name_table}"
    get_data = []
    try:
        db = sqlite3.connect(name_dbase)
        con = db.cursor()
        print(f"Connected to SQLite")
        get_data = list(con.execute(request_sql))
        parse_data(get_data)


    except sqlite3.Error as error:
        print(f"[-]ERROR  SQLite table=[ {name_table} ]  when requesting data = ", error)
    finally:
        if db:
            db.close()
            print(f"The SQLite connection is closed\n")
        return get_data


name_dbase = "q1.db"
table = "customers"
request_sql = f"SELECT * FROM {table} WHERE grade>200 ORDER BY id LIMIT 5"
data = get_all_data(name_table=table, request_sql=request_sql)





def get_name_collums(name_table="my_table") -> list:
    try:
        db = sqlite3.connect(name_dbase)
        con = db.cursor()
        print(f"Connected to SQLite")
        get_data = list(con.execute(f"PRAGMA table_info({name_table})"))
        print(f"get_data: {get_data}")
        name_collums = [row[1] for row in get_data]
        print(f"name_collums: {name_collums}")
    except sqlite3.Error as error:
        print(f"[-]ERROR  SQLite table=[ {name_table} ]  when requesting data = ", error)
    finally:
        if db:
            db.close()
            print(f"The SQLite connection is closed\n")
        return name_collums


def get_dataframe(name_table="my_table", request_sql=None) -> tuple:

    if request_sql is None:
        request_sql = f"SELECT * FROM {name_table}"
    get_data = []
    try:
        db = sqlite3.connect(name_dbase)
        con = db.cursor()
        print(f"Connected to SQLite")
        get_data = list(con.execute(request_sql))

    except sqlite3.Error as error:
        print(f"[-]ERROR  SQLite table=[ {name_table} ]  when requesting data = ", error)
    finally:
        if db:
            db.close()
            print(f"The SQLite connection is closed\n")
        return get_data


name_dbase = "rossia_loser.db"
collums = get_name_collums(name_table="total_losses")

df = get_dataframe(name_table="total_losses")
print(collums)
for row in df:
    print(row)
print(collums)
