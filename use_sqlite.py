import sqlite3

conn=sqlite3.connect("database.db")#if a database not exists python will create it

#Create a table :first retrieve cursor
myCursor=conn.cursor() #cursor allow to excute sql request

myCursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
     first_name text,
     name text
)
""")
conn.commit()
conn.close() #close connection