"""
You've 2 options: memory storage or disk storage with json file
"""
from tinydb import TinyDB, Query, where  # added Query and where   => to make a search

# let use on DISK:you can add indent parameter
db = TinyDB('app_tinydb_disk_storage.json', indent=4)


users = db.table("Users")
roles = db.table("Roles")

# INSERT ONE BY ONE
users.insert({"name": "Bonevy", "salary": 15000000})
users.insert({"name": "Laurore", "salary": 20000000})
users.insert({"name": "Ketsia", "salary": 8000000})

# MULTIPLE INSERT
roles.insert_multiple([
    {"name": "Java_Dev"},
    {"name": "Python_Dev"},
    {"name": "DotNet_Dev"}
])
