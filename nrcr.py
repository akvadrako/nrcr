# http://doodle.com/poll/sz94cavn8r4657d2

from selenium import webdriver

# HTTP_PAGE = "http://doodle.com/poll/sz94cavn8r4657d2"
# HTTP_PAGE = "http://doodle.com/poll/45apuevsy5k9a3c28p7kk7km/admin"
HTTP_PAGE = "http://doodle.com/poll/yp4snzyx6cp3pwi5"

option_list = []

browser = webdriver.PhantomJS()
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

print("pause")

name_field = browser.find_element_by_id('pname')
name_field.send_keys('user')
print name_field

savebtn = browser.find_element_by_id('save')
print savebtn
print savebtn.click()
print browser.current_url
import time
time.sleep(2)
print browser.current_url

from email.mime.text import MIMEText
msg = MIMEText('''\
    yaaa - massage
    
    {}

'''.format(browser.current_url))
msg['Subject'] = 'Massage'
msg['From'] = 'dev@doubly.so'
msg['To'] = 'dev@doubly.so'

import smtplib
s = smtplib.SMTP('nlhfd-msg001.domain1.intra')
s.sendmail('dev@doubly.so', ['dev@doubly.so'], msg.as_string())
s.quit()

print msg.as_string()
print 'email sent'


