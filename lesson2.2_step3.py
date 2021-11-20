from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    suma = num1+num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(suma))

    
    but =  browser.find_element_by_tag_name("button")
    but.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
