import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TheInternetTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_login(self):
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Form Authentication').click()


if __name__ == '__main__':
    unittest.main()
