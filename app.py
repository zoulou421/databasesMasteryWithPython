import json

file_path ="settings.json"

with open(file_path, "r") as f:
    settings = json.load(f)

print(settings)