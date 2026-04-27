import json

with open("tasks.json", "r") as file:
    data = json.load(file)

print(data)