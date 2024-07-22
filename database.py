import sqlite3
connection = sqlite3.connect('insurance.db')


query = """
create table project 
(age integer ,gender integer , bmi integer , children integer , region varchar(5),
smoker integer , health integer , prediction varchar(10))""" 


query_to_fetch = """
select * from project
"""



cur = connection.cursor()
#cur.execute(query)
#print("your database and your table is created! ")
cur.execute(query_to_fetch)
for record in cur.fetchall():
    print(record)  

cur.close()
connection.close()