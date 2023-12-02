import json
from module import header_generate
from notice_methods import deskt_wechat
from get_price import xs10
from module.save_data import update_data
from module.read_data import read

# 加載數據
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 請求的頁面
amazon_url = config['web']['x-s10'].replace('%', '%%')
# print(amazon_url)
headers = {
    "User-Agent": header_generate.user_agent()
}
# print(headers)

# 相機價格
xs10_name = 'xs10_1045kit'
xs10_price = xs10.find_price(url=amazon_url, headers=headers)
# print(xs10_price)
table = update_data(xs10_name, xs10_price)
# print(table)

# 更新数据
update_data(product_name=xs10_name,price=xs10_price)

# 读取数据
table = read()
# print(data)
deskt_wechat.send_by_wechat(table)


