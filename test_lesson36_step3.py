#Модуль для тестов
import pytest
from selenium import webdriver
import time
import math
#Мдуль для ожидания
from selenium.webdriver.support.ui import WebDriverWait as wait
#проверка элементов
from selenium.webdriver.support import expected_conditions as EC
#поиск элементов
from selenium.webdriver.common.by import By


#фикстура которая запускаеться при каждом новом вызове функции
@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class TestAnswer():
    text = ""
        
    @pytest.mark.parametrize('link', [
            "https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1",
    ])
    def test_guest(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(10)
        answer = browser.find_element_by_css_selector("textarea")
        answer.send_keys(str(math.log(int(time.time()))))
        btn = wait(browser, 20).until(EC.element_to_be_clickable(( By.CSS_SELECTOR, "button.submit-submission")))
        btn.click()
        result = wait(browser, 20).until(EC.visibility_of_element_located(( By.CSS_SELECTOR, ".smart-hints__hint"))).text
        if result != "Correct!":
            TestAnswer.text += result
        print(TestAnswer.text)
        assert result == "Correct!"




    
