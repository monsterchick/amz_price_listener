import datetime
from module.header_generator import header_generate
from listen_logit.get_xs10_price import find_price
import tabulate
from module.json_operator import Json
from notice_methods.deskt_wechat import Script


class Main:
    def __init__(self):
        # 初始化當前時間
        self.current_time = None

        # 初始化價格
        self.product_price = None

        # 初始化腳本實例
        self.s = Script()

        # 加載config.json數據
        self.j = Json('config.json')
        self.config_data = self.j.read_json()

        # 加載data.json數據
        self.jd = Json('data.json')
        self.data = self.jd.read_json()

        # 加載隨機header
        self.headers = header_generate()

    def make_datetime(self):
        current_datetime = datetime.datetime.now()
        formatted_string = current_datetime.strftime("%Y%m%d_%H:%M:%S")
        self.current_time = formatted_string
        return formatted_string

    def tbl_message(self, product_name, product_price, current_time):
        # 製作表格
        header = ['product', 'price', 'datetime']
        data = [
            [product_name, product_price, current_time]
        ]
        colalign = ("center", "center", "center")
        table = tabulate.tabulate(data, headers=header, tablefmt='Plain', colalign=colalign)
        return table

    def xs10_listen(self):
        # 請求地址
        url = self.config_data['url']['xs10']

        # 產品名字
        product_name = list(self.config_data['url'].keys())[0]
        # print('lllll',product_name)
        # 當前時間
        current_time = self.make_datetime()
        # 相機價格
        self.product_price = find_price(url=url, headers=self.headers)

        # print('22222aa', self.product_price)
        # print('ddddd', self.config_data)
        # print('kkkk', product_name)

        # 保存產品信息到本地
        data_update = {
            '{}'.format(product_name):
                {
                    'name': product_name,
                    'price': self.product_price,
                    'current_time': current_time
                }
        }
        # data_update = {
        #     'test':
        #         {
        #             'name': 'test_prod',
        #             'price': 1314,
        #             'current_time': current_time
        #         }
        # }

        # 文件不為空，更新數據
        self.jd.update_json(data_update)

        # 製作消息內容
        tbl_message = self.tbl_message(product_name, self.product_price, self.current_time)
        # print('77777777', self.current_time)

        # 判斷價格變動 + 電腦微信自動化
        self.s.send_by_wechat(tbl_message)

    # def xs10_listen(self):
    #     # 相機價格
    #     xs10_price = find_price(url=self.config_data['url']['xs10'], headers=self.headers)
    #     # print(xs10_price)
    #
    #     tbl_message = self.tbl_message(xs10_price)
    #
    #     self.s.send_by_wechat(tbl_message)


m = Main()
m.xs10_listen()
