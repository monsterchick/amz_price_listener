import datetime
from tabulate import tabulate
import json


def generate_date():
    current_datetime = datetime.datetime.now()
    # print(current_datetime)
    formatted_datetime = current_datetime.strftime("%Y%m%d_%H:%M:%S")
    return formatted_datetime

def update_data(product_name, price):

    # headers = ['产品', '价格', '更新']
    headers = ['item', 'price', 'datetime']

    data = []
    data.append([product_name, price, generate_date()])

    data = {
        "headers": headers,
        "data": data
    }

    with open("save_data.json", "w") as json_file:
        json.dump(data, json_file, indent=2)


