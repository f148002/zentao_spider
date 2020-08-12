from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from save import save
import time
from get_ids import get_ids

chrome_options = Options()
chrome_options.add_argument('--save-page-as-mhtml')
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=chrome_options)

def ele(loc):
    return browser.find_element(*loc)

def sub_text(ele, loc):
    return ele.find_element(*loc).text

def eles(loc):
    return browser.find_elements(*loc)

button_root = (By.CSS_SELECTOR,'tr[data-id]')

button_id = (By.CSS_SELECTOR,'a[href]')
button_title = (By.CSS_SELECTOR,'.c-title.text-left')
button_real_title =(By.CSS_SELECTOR,'a[href]')

button_status = (By.CSS_SELECTOR,'.status-bug')
button_creator = (By.CSS_SELECTOR,'.c-openedBy')
button_created_date = (By.CSS_SELECTOR,'.c-openedDate')
button_asignto = (By.CSS_SELECTOR,'.c-assignedTo')

all_lines = eles(button_root)

print('开始获取列表')
items = []
for line in all_lines:
    item = {
        # 'title': line.find_element(*button_title).find_element(*button_real_title).text,
        'url': line.find_element(*button_title).find_element(*button_real_title).get_attribute('href'),
        'id': sub_text(line, button_id),
        # 'status': sub_text(line, button_status),
        # 'creator': sub_text(line, button_creator),
        # 'created_date': sub_text(line, button_created_date),
        # 'asignto': sub_text(line, button_asignto),
    }
    items.append(item)


all_ids = get_ids()

print('开始保存网页')
time.sleep(5)
for a in items:
    if a['id'] not in all_ids:
        save(browser, a.get('url'))
        time.sleep(0.5)

print('成功')