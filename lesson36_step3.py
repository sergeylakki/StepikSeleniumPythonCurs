from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://stepik.org/lesson/236895/step/1")
browser.implicitly_wait(10)
answer = browser.find_element_by_css_selector("textarea")



answer.send_keys(str(math.log(int(time.time()))))
btn = wait(browser, 20).until(EC.element_to_be_clickable(( By.CSS_SELECTOR, "button.submit-submission")))
btn.click()


result = wait(browser, 20).until(EC.visibility_of_element_located(( By.CSS_SELECTOR, ".smart-hints__hint"))).text
assert result == "Correct!"
browser.quit()

