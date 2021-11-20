from selenium import webdriver
import math
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    label = browser.find_element_by_css_selector("#input_value")
    ask = calc(int(label.text))

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(ask)

    radioButton = browser.find_element_by_css_selector("#robotsRule")
    radioButton.click()
    chek = browser.find_element_by_css_selector("#robotCheckbox")
    chek.click()

    print(ask)
    but =  browser.find_element_by_tag_name("button")
    but.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".first[placeholder='Input your first name']")
    input1.send_keys("Ivan")

    input1 =  browser.find_element_by_css_selector(".second[placeholder='Input your last name']")
    input1.send_keys("Ivanovich")

    input1 =  browser.find_element_by_css_selector(".third[placeholder='Input your email']")
    input1.send_keys("email")
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
