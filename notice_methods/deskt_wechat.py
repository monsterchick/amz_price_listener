import json
import time
import pyautogui
import pyperclip
# from module.image_path import find_image_path
from module.path_operator import Path


class Script:
    def __init__(self):
        self.p = Path()


    def send_by_wechat(self,table):
        group_icon_location = pyautogui.locateOnScreen(self.p.smart_file_path('test.png'), confidence=0.7)
        print('1111111111111',self.p.smart_file_path('test.png'))
        group_icon_center = pyautogui.center(group_icon_location)
        pyautogui.moveTo(group_icon_center)
        pyautogui.click()
        time.sleep(1)

        # 發送消息
        emoji_area_location = pyautogui.locateOnScreen(self.p.smart_file_path('emoji.png'), confidence=0.7)
        emoji_center = pyautogui.center(emoji_area_location)
        pyautogui.moveTo(emoji_center)
        print(self.p.smart_file_path('emoji.png'))
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