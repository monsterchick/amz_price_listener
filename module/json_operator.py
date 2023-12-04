import json
from json.decoder import JSONDecodeError
from module.path_operator import Path


class Json:
    def __init__(self, file_name):
        p = Path()
        self.file_path = p.smart_file_path(file_name)

    def read_json(self):
        try:
            with open(self.file_path, mode='r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return None
        except JSONDecodeError:
            # 如果文件是空的，返回空字典
            return {}

    def write_json(self, data):
        with open(self.file_path, mode='w') as file:
            json.dump(data, file, indent=4)
        print(f'JSON 文件更新成功：{self.file_path}')

    def update_json(self, update_data):
        try:
            existing_data = self.read_json()

            # 如果文件內有數據
            if existing_data:
                existing_data.update(update_data)
                self.write_json(existing_data)

            else:
                # 如果文件內沒有數據，直接寫入新提供的數據
                self.write_json(update_data)
                print('文件為空')

        except JSONDecodeError:
            print('文件可能不存在或 JSON 解碼錯誤')


# 使用例子
# j = Json('config_data.json')
# j.update_json({'ttt': 'rrr'})
