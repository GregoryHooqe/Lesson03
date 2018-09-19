import csv
user_list = [
    {'name': 'Masha', 'age': '25', 'job': 'Scientist'},
    {'name': 'Vasya', 'age': '8', 'job': 'Programmer'},
    {'name': 'Eduard', 'age': '48', 'job': 'Big Boss'},
]

with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)


