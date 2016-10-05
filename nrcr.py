from selenium import webdriver
import re
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#HTTP_PAGE = "http://doodle.com/poll/sz94cavn8r4657d2"
HTTP_PAGE = "http://doodle.com/poll/45apuevsy5k9a3c28p7kk7km/admin"
prefered_time = datetime.strptime('10:00 AM', '%H:%M %p')
my_name = 'xinyue'
option_list = []

def get_option(option_list):
    min_delta = 86400.0  # seconds/day
    for option in option_list:
        time_raw = (option.get_attribute("title"))
        time_reg = re.match(r"(.*?)(\d+:\d+ (A|P)M)", time_raw)
        selected_time = datetime.strptime(time_reg.group(2), '%H:%M %p')
        time_delta = abs((selected_time - prefered_time).total_seconds())
        if time_delta < min_delta:
            min_delta = time_delta
            my_option = option
    return my_option

browser = webdriver.Firefox()
browser.get(HTTP_PAGE)
browser.maximize_window()
try:
    elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.header.date.month th.asep")))
    elem.click()
except TimeoutException:
    pass

event_list = browser.find_elements_by_css_selector('tr.participation.yesNo.partMyself td:not(.disabled)')

for event in event_list[1:]:
#for event in browser.find_elements_by_css_selector('tr.participation.yesNo.partMyself td.disabled')[1:]:
    option_list.append(event)

if option_list:
    pname_list = browser.find_elements_by_id('pname')
    if pname_list:
        pname_list[0].send_keys(my_name)
        option = get_option(option_list)
        option.click()
        button_list = browser.find_elements_by_id('save')
        if button_list:
            button_list[0].click()

browser.quit()
