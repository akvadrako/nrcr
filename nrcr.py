# http://doodle.com/poll/sz94cavn8r4657d2
from selenium import webdriver
import re
from datetime import datetime

HTTP_PAGE = "http://doodle.com/poll/sz94cavn8r4657d2"
#HTTP_PAGE = "http://doodle.com/poll/45apuevsy5k9a3c28p7kk7km/admin"
prefered_time = datetime.strptime('10:20 AM', '%H:%M %p')
min_delt = 0.0

option_list = []

browser = webdriver.Firefox()
browser.get(HTTP_PAGE)

# elem = browser.find_element_by_id('box0')
# elem = browser.find_elements_by_name('header time')
elem = browser.find_elements_by_css_selector('tr.participation td')

# browser.find_elements_by_css_selector('tr.participation td:not(.disabled)')[1:][0].click()
# browser.find_element_by_id('option0').is_selected()

for event in browser.find_elements_by_css_selector('tr.participation td:not(.enabled)')[1:]:
    option_list.append(event)

# browser.find_elements_by_css_selector('tr.participation td:not(.disabled)')[1:][0].get_attribute("title")
for event in option_list:
    option = (event.get_attribute("title"))
    # regex = re.compile(r'\d+:\d+')
    my_option = re.match(r"(.*?)(\d+:\d+ (A|P)M)", option)
    date = datetime.strptime(my_option.group(2), '%H:%M %p')
    delt= abs((date - prefered_time).total_seconds())
    print(delt)

print("pause")
# elem.click()





