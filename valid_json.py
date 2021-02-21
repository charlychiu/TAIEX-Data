import json

with open("20000104-20210219-k.json", 'r') as f:
    data = json.loads(f.read())

print(data['2021/02/19'])