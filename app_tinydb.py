"""
You've 2 options: memory storage or disk storage with json file
"""
from tinydb import TinyDB

# the following import will allow you to use MEMORY STORAGE
from tinydb.storages import MemoryStorage

# Disk storage option
# db = TinyDB('data_tinydb.json')  # it will create database:data_tinydb.json
# db=TinyDB(storage=MemoryStorage)  # allowing to use in memory method

# let use on DISK:you can add indent parameter
db = TinyDB('data_tinydb.json', indent=4)
db.insert({"name": "Bonevy", "Score": 100})
