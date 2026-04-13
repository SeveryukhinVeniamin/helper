import csv
import json

data = {}
with open('data.csv', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=':')
    for line in list(reader)[1:]:
        if line[4] not in data:
            data[line[4]] = {'salaries': [float(line[3])], 'ages': [int(line[2])], 'names': [line[1]]}
        else:
            data[line[4]]['salaries'].append(float(line[3]))
            data[line[4]]['ages'].append(int(line[2]))
            data[line[4]]['names'].append(line[1])
new_data = {}
for key in data:
    new_data[key] = {'name': min(data[key]['names']), 'age': sum(data[key]['ages'])/len(data[key]['ages']), 'salary': max(data[key]['salaries'])}



with open('data.json', 'w', encoding="utf-8") as f:
    json.dump(new_data, f)