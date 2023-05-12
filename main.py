import json

with open("items.json", "r") as f:
    json_items = json.load(f)
with open("entities.json", "r") as f:
    json_entities = json.load(f)