import sqlite3

conn = sqlite3.connect("database.db")  # if a database not exists python will create it

# Create a table :first retrieve cursor
myCursor = conn.cursor()  # cursor allow to execute sql request
'''
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
'''
myCursor.execute("""
CREATE TABLE IF NOT EXISTS employees_update(
     first_name test,
     last_name text,
     salary int
)
""")
#INSERT
dic = {"a": "Bonevy", "b": "BEBY", "c": 5987}
conn.execute("INSERT INTO employees_update VALUES(:a, :b,:c)", dic)

#UPDATE
dic_v2 = {"salary": 35000, "first_name": "Bonevy", "last_name": "BEBY"}
myCursor.execute("""UPDATE employees_update SET salary=:salary
WHERE first_name=:first_name AND last_name=:last_name
""", dic_v2)

#DELETE
myCursor.execute("DELETE FROM employees WHERE first_name='Bonevy'")

conn.commit()
conn.close()  # close connection

#link EXTERNAL SQLITE DOWNLOAD: https://sqlitebrowser.org/dl/
