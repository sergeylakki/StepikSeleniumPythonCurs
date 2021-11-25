import unittest
from selenium import webdriver

class TestReg(unittest.TestCase):

  def setup(self):
    self.browser = webdriver.Chrome()
    
    
  def test_reg_form1(self):
    self.browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/registration1.html"
    self.browser.get(link)

    input1 = self.browser.find_element_by_css_selector(".first[placeholder='Input your first name']")
    input1.send_keys("Ivan")

    input1 =  self.browser.find_element_by_css_selector(".second[placeholder='Input your last name']")
    input1.send_keys("Ivanovich")

    input1 =  self.browser.find_element_by_css_selector(".third[placeholder='Input your email']")
    input1.send_keys("email")

    # Отправляем заполненную форму
    button = self.browser.find_element_by_css_selector("button.btn")
    button.click()
    # находим элемент, содержащий текст
    welcome_text_elt = self.browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


  def test_reg_form2(self):
    self.browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/registration2.html"
    self.browser.get(link)

    input1 = self.browser.find_element_by_css_selector(".first[placeholder='Input your first name']")
    input1.send_keys("Ivan")

    input1 =  self.browser.find_element_by_css_selector(".second[placeholder='Input your last name']")
    input1.send_keys("Ivanovich")

    input1 =  self.browser.find_element_by_css_selector(".third[placeholder='Input your email']")
    input1.send_keys("email")

     # Отправляем заполненную форму
    button = self.browser.find_element_by_css_selector("button.btn")
    button.click()
    # находим элемент, содержащий текст
    welcome_text_elt = self.browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")



if __name__ == "__main__":
    unittest.main()
