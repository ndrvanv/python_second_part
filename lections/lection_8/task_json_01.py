import json

with open('C:/Users/1311103/OneDrive/Рабочий стол/GB/python_2/lections/lection_8/user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["mother"]["name"] = }')
