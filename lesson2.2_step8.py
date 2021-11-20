from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("input[placeholder='Enter first name']")
    input1.send_keys("Ivan")

    input1 =  browser.find_element_by_css_selector("input[placeholder='Enter last name']")
    input1.send_keys("Ivanovich")

    input1 =  browser.find_element_by_css_selector("input[placeholder='Enter email']")
    input1.send_keys("email")


    
    file = browser.find_element_by_id("file")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)



    
    but =  browser.find_element_by_tag_name("button")
    but.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
