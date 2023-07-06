import time
import unittest

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class ContactUsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_homepage(self):
        driver = self.driver
        driver.get("http://uitestingplayground.com/home")

    def test_contact_form_submission(self):
        # Навигация на страницу с контактной формой
        self.driver.get("https://www.globalsqa.com/contact-us/")

        # Нахожу элементы формы и заполняю значения
        name_input = self.driver.find_element(By.ID, "comment_name")
        name_input.send_keys("John Doe")

        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys("johndoe@example.com")

        subject_input = self.driver.find_element(By.ID, "subject")
        subject_input.send_keys("Regarding Inquiry")

        message_input = self.driver.find_element(By.ID, "comment")
        message_input.send_keys("Hello, I have a question.")

        # Решаю капчу
        captcha_image = self.driver.find_element(By.XPATH, "//div[@class='g-recaptcha']/div/div/iframe")
        captcha_image_url = captcha_image.get_attribute("src")
        response = requests.get(captcha_image_url)
        with open("captcha.png", "wb") as f:
            f.write(response.content)

        # Ожидаем, пока юзер решает капчу и отправляет форму вручную
        time.sleep(110)


if __name__ == '__main__':
    unittest.main()
