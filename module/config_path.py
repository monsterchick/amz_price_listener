import json
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(root_dir,__file__)


def find_config_path():
    config_path = os.path.join(root_dir,'config.json')
    with open(config_path,'r') as f:

        config_path = os.path.join(root_dir,json.load(f)['json_path'])

        # print(config_path)
        return config_path