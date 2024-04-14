import sqlite3

conn = sqlite3.connect("database.db")  # if a database not exists python will create it

# Create a table :first retrieve cursor
myCursor = conn.cursor()  # cursor allow to excute sql request

myCursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
     first_name text,
     name text
)
""")
dic = {"a": "Bonevy", "b": "BEBY"}
conn.execute("INSERT INTO employees VALUES(:a, :b)", dic)
d = {"a": "Bonevy"}
myCursor.execute("SELECT *FROM employees WHERE first_name=:a", d)
myData=myCursor.fetchall() #represents a generator and can only be executed one time per request//
#also see: fetchone and test it.

print(myData)
conn.commit()
conn.close()  # close connection
