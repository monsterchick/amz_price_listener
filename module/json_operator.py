import json
from module.path_operator import Path


class Json:
    def __init__(self, file_name):
        p = Path()
        self.file_path = p.smart_file_path(file_name)
        # print(self.file_path)

    def read_json(self):
        with open(self.file_path, mode='r') as file:
            data = json.load(file)
            return data

    def write_json(self, data):
        print(type(data))
        with open(self.file_path, mode='w') as file:
            json.dump(data, file, indent=4)

    def update_json(self, update_data):
        existing_data = self.read_json()
        # print(type(existing_data))
        # 文件內有數據的情況下
        if existing_data is not None:
            existing_data.update(update_data)
            self.write_json(existing_data)
        else:
            print(f'json 文件更新成功：{self.file_path}')

# j = Json('save_data.json')
# print(j.load_json_file())
# j.write_json({'asfd':'asdfasdf'})
# j.update_json({'ttt':'rrr'})