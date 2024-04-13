import json

file_path ="settings.json"

with open(file_path, "r") as f:
    settings = json.load(f)

print(settings) #key:value
settings["fontSize"]=30

with open(file_path, "w") as f:
      json.dump(settings,f, indent=4)

print(settings.get("fontSize"))#value
