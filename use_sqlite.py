import sqlite3

conn=sqlite3.connect("database.db")#if a database not exists python will create it
conn.close() #close connection