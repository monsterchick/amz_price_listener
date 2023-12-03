from module import json_operator

from module import path_operator
j = json_operator.Json('config.json')
p = path_operator.Path()
file_name = p.smart_file_path('config.json')
data = j.read_json()
print(data)
print(data['url'])
print(list(data['url'].keys())[0])
