import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


class BankingProjectTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        try:
            alert = cls.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            print(f"Unexpected alert present with text: {alert_text}")
        except NoAlertPresentException:
            pass
        finally:
            cls.driver.close()
            cls.driver.quit()

    def test_login(self):
        self.driver.get('http://www.demo.guru99.com/V4/')
        self.driver.find_element(By.NAME, 'uid').send_keys('username')
        self.driver.find_element(By.NAME, 'password').send_keys('password')
        self.driver.find_element(By.NAME, 'btnLogin').click()


if __name__ == '__main__':
    unittest.main()
