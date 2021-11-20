from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id("input_value").text)
    inputX = browser.find_element_by_id("answer")
    inputX.send_keys(calc(x))


    but =  browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", but)

    radioButton = browser.find_element_by_css_selector("#robotsRule")
    radioButton.click()
    chek = browser.find_element_by_css_selector("#robotCheckbox")
    chek.click()
    
    but =  browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", but)
    but.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
