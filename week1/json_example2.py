import json

with open('sample1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data)