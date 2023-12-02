import re
import json
from module import header_generate
from bs4 import BeautifulSoup
from find_price import xs10

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

xs10_price = xs10.find_price(url=amazon_url, headers=headers)
print(xs10_price)

