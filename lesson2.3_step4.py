from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/alert_accept.html"

    
    browser = webdriver.Chrome()
    browser.get(link)

    but =  browser.find_element_by_tag_name("button")
    but.click()

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)

    x = int(browser.find_element_by_id("input_value").text)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))

    but =  browser.find_element_by_tag_name("button")
    but.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
