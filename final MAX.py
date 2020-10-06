import json
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.maximize_window()
import time

print('opening the link https://api.encoding.com ')
driver.get('https://api.encoding.com')
search_box = driver.find_element(By. CLASS_NAME, 'searchbox')
search_box.click()
time.sleep(3)
search_box_input = driver.find_element(By.CLASS_NAME, 'Input')
search_box_input.send_keys('getStatus')

time.sleep(3)
status_extended_link = driver.find_element(By.XPATH, "//header[@title='(GET) GetStatus (extended)']")
status_extended_link.click()
time.sleep(8)
browser = driver.current_url
print(browser)
url_check = 'https://api.encoding.com/reference/responses-getstatus-extended'
if browser == url_check:
    print("url " + browser + " is ok")
else:
    print('something is wrong')

print("going to Json part")

json_button = driver.find_elements(By.XPATH, "//button[@type = 'button']")
json_button = json_button[3].click()

json_table = driver.find_elements(By.XPATH, "//code[@class='rdmd-code lang-json']")
json_table = json_table[1]
json_text = json_table.text
json_text = json.loads(json_text)

print('obtaining json keys and values')

json_processor = json_text["response"]["job"][0]["processor"]
print(json_processor)
if "AMAZON" and "RACKSPACE" in json_processor:
    print("processor values are ok")
else:
    print('something is going wrong')

json_status = json_text["response"]["job"][0]["format"][0]["status"]
print(json_status)
if "Status" in json_status:
    print('json status is ok')
else:
    print("something is going wrong")
