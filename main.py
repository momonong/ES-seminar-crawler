import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# 載入 .env 檔案中的設定
load_dotenv()

URL = os.getenv("URL")
PREVIOUS_VALUE = os.getenv("PREVIOUS_VALUE")
LINE_NOTIFY_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")
LINE_NOTIFY_API = os.getenv("LINE_NOTIFY_API")

def update_previous_value(new_value):
    with open('.env', 'r') as file:
        content = file.readlines()

    updated_content = []
    for line in content:
        if line.startswith('PREVIOUS_VALUE='):
            updated_content.append(f'PREVIOUS_VALUE={new_value}\n')
        else:
            updated_content.append(line)

    with open('.env', 'w') as file:
        file.writelines(updated_content)

def send_line_notify(message):
    headers = {
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
    }
    data = {
        'message': message
    }
    response = requests.post(LINE_NOTIFY_API, headers=headers, data=data)
    return response.status_code

def check_element_change():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 首先找到名稱為'semid'的<select>元素
    select_element = soup.find('select', {'name': 'semid'})

    # 在該<select>元素中找到被選中的<option>元素
    option_element = select_element.find('option', selected=True)
    
    if option_element:
        current_value = option_element.text
        if PREVIOUS_VALUE and PREVIOUS_VALUE != current_value:
            print("seminar has updated!!")
            send_line_notify(f"seminar has updated!!\n\n{URL}")  # 發送LINE通知
            update_previous_value(current_value)  # 更新 .env 檔案中的 PREVIOUS_VALUE
        else:
            # send_line_notify(f'nothing changed: {current_value}')
            print(f"Element remains the same. {current_value}")
    else:
        print("Element not found!")

# 執行檢查
check_element_change()
