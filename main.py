import datetime
from module.header_generator import header_generate
from listen_logit.get_xs10_price import find_price
import tabulate
from module.json_operator import Json
from notice_methods.deskt_wechat import Script


class Main:
    def __init__(self):
        self.s = Script()

        # 加載config.json數據
        j = Json('config.json')
        self.data = j.read_json()
        # 加載隨機header
        self.headers = header_generate()

        # list(self.data['url'].keys())[0]
        print(list(self.data['url'].keys())[0])

    def make_datetime(self):
        current_datetime = datetime.datetime.now()
        formatted_string = current_datetime.strftime("%Y%m%d%H:%M:%S")
        return formatted_string

    def tbl_message(self,price):
        header = ['product', 'price', 'date']
        data = [
            [list(self.data['url'].keys())[0], price, self.make_datetime()]
        ]

        colalign = ("center", "center", "center")
        table = tabulate.tabulate(data, headers=header, tablefmt='Plain',colalign=colalign)
        return table

    def xs10_listen(self):
        # 相機價格
        xs10_price = find_price(url=self.data['url']['xs10'], headers=self.headers)
        print(xs10_price)

        tbl_message = self.tbl_message(xs10_price)

        self.s.send_by_wechat(tbl_message)

m = Main()

m.xs10_listen()



