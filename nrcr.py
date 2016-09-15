# http://doodle.com/poll/sz94cavn8r4657d2

from selenium import webdriver
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

username = config['default']['username']
email = config['default']['email']
prefered_time = config['default']['prefered_time']

print(username, email, prefered_time)

# HTTP_PAGE = "http://doodle.com/poll/sz94cavn8r4657d2"
HTTP_PAGE = "http://doodle.com/poll/45apuevsy5k9a3c28p7kk7km/admin"

option_list = []

browser = webdriver.Firefox()
browser.get(HTTP_PAGE)

# elem = browser.find_element_by_id('box0')
# elem = browser.find_elements_by_name('header time')
elem = browser.find_elements_by_css_selector('tr.participation td')

# browser.find_elements_by_css_selector('tr.participation td:not(.disabled)')[1:][0].click()
# browser.find_element_by_id('option0').is_selected()

for event in browser.find_elements_by_css_selector('tr.participation td:not(.disabled)')[1:]:
    option_list.append(event)

# browser.find_elements_by_css_selector('tr.participation td:not(.disabled)')[1:][0].get_attribute("title")

for event in option_list:
    print(event.get_attribute("title"))

browser.quit()

# print("pause")
# elem.click()





