"""
You've 2 options: memory storage or disk storage with json file
"""
from tinydb import TinyDB, Query, where  # added Query and where   => to make a search

# the following import will allow you to use MEMORY STORAGE
from tinydb.storages import MemoryStorage

# Disk storage option
# db = TinyDB('data_tinydb.json')  # it will create database:data_tinydb.json //this is a relative path
# db=TinyDB(storage=MemoryStorage)  # allowing to use in memory method

# let use on DISK:you can add indent parameter
db = TinyDB('data_tinydb.json', indent=4)
# db.insert({"name": "Bonevy", "Score": 100})
# Multiline insert
"""db.insert_multiple([
    {"name": "Bonevy", "Score": 100},
    {"name": "Laurore", "Score": 900}
])"""

# SEARCH
User = Query()
my_user = db.search(User.name == "Bonevy")  # replace db.search to get =>for unique retrieve//unique object
print(my_user)

# USE CONDITION
higher_scores = db.search(where("Score") > 100)
print(higher_scores)

'''name1 = db.search(where("name") == "Bonevy")
print(name1)

print(db.contains(User.name == "Laurore"))

# COUNT
print(db.count(User.name == "Laurore"))'''

'''
# UPDATE
db.update({"Score": 999}, where('name') == 'Laurore')

db.update({"roles": ["Senior"]})  # every user updated and field roles added
db.update({"roles": ["Python_Dev"]}, where('name') == 'Laurore') #role changed to Python_Dev
'''
# Other method of update:upsert
db.upsert({"name": "Ketsia", "Score": 100, "roles": ["Junior"]}, where('name') == "Laurore")

# REMOVE
db.remove(where('Score') == 1003)

#REMOVE DATA :truncate()
db.truncate()
