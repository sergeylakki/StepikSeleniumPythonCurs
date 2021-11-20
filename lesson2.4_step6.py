from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/cats.html"

    
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_id("button")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
