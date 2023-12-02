import json
from tabulate import tabulate


def read():
    # 从 JSON 文件中读取数据
    with open("save_data.json", "r") as json_file:
        loaded_data = json.load(json_file)

    # 提取表头和数据
    headers = loaded_data["headers"]
    data = loaded_data["data"]

    # 生成表格
    table = tabulate(data, headers, tablefmt="simple", colalign=("center", "center", "center"))

    # 打印表格或进行其他操作
    # print(table)
    return table

