import json
import requests

'''data = []
with open('data.jsonl') as f:
    for i in f:
        data.append(json.loads(i))

print(data)'''

request = f'http://127.0.0.1:5000/3'

response = requests.get(request)
print(response.json())
