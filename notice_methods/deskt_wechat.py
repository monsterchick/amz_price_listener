import json
import time
import pyautogui
import pyperclip
from module.image_path import find_image_path
from module.save_data import update_data

def send_by_wechat(table):
    # 讀取json檔案
    with open('config.json') as f:
        data = json.load(f)
        test_image_name = data['image_path']['test']
        emoji_image_name = data['image_path']['emoji']

    location = pyautogui.locateOnScreen(find_image_path(test_image_name), confidence=0.7)
    center = pyautogui.center(location)
    pyautogui.moveTo(center)
    pyautogui.click()
    time.sleep(1)

    # 發送消息
    emoji_location = pyautogui.locateOnScreen(find_image_path(emoji_image_name), confidence=0.7)
    emoji_center = pyautogui.center(emoji_location)
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

