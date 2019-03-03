""" Implicit Wait """
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
import sys

""" for firefox """
# profile = webdriver.FirefoxProfile('/home/sirius0027/.mozilla/firefox/m2iyw7tf.default')
# driver = webdriver.Firefox(executable_path = '../firefox/geckodriver', firefox_profile = profile)

""" for chrome """
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=/home/sirius0027/.config/google-chrome/')
driver = webdriver.Chrome(executable_path = '../chrome/chromedriver', options = options)

driver.implicitly_wait(60)
target = sys.argv[1]
message = sys.argv[2]
try:
    driver.get("https://web.whatsapp.com/")
    x_arg = '//span[@title="{}"]'.format(target)
    for i in range(3):
        title = driver.find_element_by_xpath(x_arg)
    title.click()
    inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(5)
except Exception as e:
    f = open("error.log", "a")
    print("Error Occured.\n Check the error.log file")
    f.write(str(e))
    f.close()
finally:
    driver.close()
