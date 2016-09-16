# http://doodle.com/poll/sz94cavn8r4657d2
from selenium import webdriver
import re
from datetime import datetime

HTTP_PAGE = "http://doodle.com/poll/sz94cavn8r4657d2"
#HTTP_PAGE = "http://doodle.com/poll/45apuevsy5k9a3c28p7kk7km/admin"
prefered_time = datetime.strptime('10:00 AM', '%H:%M %p')
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

# elem = browser.find_element_by_id('box0')
# elem = browser.find_elements_by_name('header time')
elem = browser.find_elements_by_css_selector('tr.participation td')

# browser.find_elements_by_css_selector('tr.participation td:not(.disabled)')[1:][0].click()
# browser.find_element_by_id('option0').is_selected()

for event in browser.find_elements_by_css_selector('tr.participation td:not(.enabled)')[1:]:
    option_list.append(event)

option = get_option(option_list)
# browser.find_elements_by_css_selector('tr.participation td:not(.disabled)')[1:][0].get_attribute("title")
print("pause")
# elem.click()





