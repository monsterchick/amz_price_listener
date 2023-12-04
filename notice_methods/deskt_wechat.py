from module.json_operator import Json
import time
import pyautogui
import pyperclip
from module.path_operator import Path


class Script:
    def __init__(self):
        self.p = Path()

        # 定位微信輸入框
        self.group_emoji_path = self.p.smart_file_path('emoji.png')

        # 定位微信群組
        self.group_laowo_path = self.p.smart_file_path('laowo.png')
        self.group_test_path = self.p.smart_file_path('test.png')
    def send_by_wechat(self,table):
        group_icon_location = pyautogui.locateOnScreen(self.group_test_path, confidence=0.7)
        group_icon_center = pyautogui.center(group_icon_location)
        pyautogui.moveTo(group_icon_center)
        pyautogui.click()
        time.sleep(1)

        # 發送消息
        emoji_area_location = pyautogui.locateOnScreen(self.group_emoji_path, confidence=0.7)
        emoji_center = pyautogui.center(emoji_area_location)
        pyautogui.moveTo(emoji_center)

        # 获取当前鼠标位置
        start_x, start_y = pyautogui.position()
        target_x = start_x
        target_y = start_y + 30
        pyautogui.moveTo(target_x, target_y)
        pyautogui.click()
        time.sleep(1)


        pyperclip.copy(table)
        time.sleep(1)
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        pyautogui.press('enter')

    # send_by_wechat('aaaaa')