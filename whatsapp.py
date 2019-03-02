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

try:
    driver.get("https://web.whatsapp.com/")
    target = '"Sabyasachi NITD"'
    message = "Scheduled Message at 16:44"
    x_arg = '//span[@title=' + target + ']'
    title = driver.find_element_by_xpath(x_arg)
    title.click()
    inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    input_box.send_keys(message + Keys.ENTER)
except Exception as e:
    f = open("error.log", "w")
    f.write(e)
    f.close()
