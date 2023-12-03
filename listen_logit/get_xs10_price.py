import re
import requests
from bs4 import BeautifulSoup


def find_price(url, headers):
    res = requests.get(url, headers=headers)
    # print('status code: ', res.status_code)
    # print(res.text)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text,'html.parser')
        selected_elements = soup.select('#corePrice_feature_div span.a-price.aok-align-center span.a-offscreen')
        # print(selected_elements)
        for element in selected_elements:
            element = str(element)
            # 使用正则表达式匹配价格部分
            pattern = re.compile(r'<span class="a-offscreen">(.*?)</span>')
            match_result = pattern.search(element)

            # 價格
            # print(match_result.group(1))
            price = match_result.group(1)
            return price
    else:
        print('Failed to fetch page. Status code: {}'.format(res.status_code))
