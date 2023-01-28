import sqlite3
conn = sqlite3.connect('q1.db')
print('Connected to SQLite')


c = conn.cursor()
c.execute("SELECT COUNT(*) FROM customers where grade>200 order by id LIMIT 10")
rows_num = c.fetchone()
print('Total rows are:   '+str(rows_num[0]))
print('Total rows are:   '+str(rows_num[0]))
print('Printing each row')
c.execute("select * from customers where grade>200 order by id")
rows = c.fetchall()
print(rows)
print('Total rows are:   '+len(rows))