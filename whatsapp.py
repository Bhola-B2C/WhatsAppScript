""" Implicit Wait """
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 

""" for firefox """
#driver = webdriver.Firefox(executable_path = './firefox/geckodriver')

""" for chrome """
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=/home/sirius0027/.config/google-chrome/')
driver = webdriver.Chrome(executable_path = '../chrome/chromedriver', options = options)

driver.implicitly_wait(60)
driver.get("https://web.whatsapp.com/")

target = '"Sabyasachi Nitd"'
message = "Test Message"

x_arg = '//span[@title=' + target + ']'
time.sleep(2)
x_arg = '//span[@title=' + target + ']'
title = driver.find_element_by_xpath(x_arg)
print(target + " found")
title.click()
print("click done")
inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
input_box = driver.find_element_by_xpath(inp_xpath)
print("input_box found")
input_box.send_keys(message + Keys.ENTER)
print("message sent")