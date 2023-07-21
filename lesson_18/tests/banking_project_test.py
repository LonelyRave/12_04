# import allure
# import pytest
# from selenium import webdriver
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.common.by import By
#
#
# @pytest.fixture(scope="class")
# def driver():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     try:
#         alert = driver.switch_to.alert
#         alert_text = alert.text
#         alert.accept()
#         print(f"Unexpected alert present with text: {alert_text}")
#     except NoAlertPresentException:
#         pass
#     finally:
#         driver.close()
#         driver.quit()
#
#
# @allure.feature("Banking Project Tests")
# class TestBankingProject:
#
#     @pytest.fixture(autouse=True)
#     def allure_attach_screenshot(self, driver, request):
#         yield
#         allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
#
#     @allure.story("Login Test")
#     def test_login(self, driver):
#         driver.get('http://www.demo.guru99.com/V4/')
#         driver.find_element(By.NAME, 'uid').send_keys('username')
#         driver.find_element(By.NAME, 'password').send_keys('password')
#         driver.find_element(By.NAME, 'btnLogin').click()
#
#     @allure.story("Registration Test")
#     def test_registration(self, driver):
#         pass
#
#     @allure.story("Contact Us Test")
#     def test_contact_us(self, driver):
#         pass
#
#
# @pytest.fixture(scope="class")
# def driver():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     try:
#         alert = driver.switch_to.alert
#         alert_text = alert.text
#         alert.accept()
#         print(f"Unexpected alert present with text: {alert_text}")
#     except NoAlertPresentException:
#         pass
#     finally:
#         driver.close()
#         driver.quit()
#
#
# @allure.feature("Banking Project Tests")
# class TestBankingProject:
#
#     @pytest.fixture(autouse=True)
#     def allure_attach_screenshot(self, driver, request):
#         yield
#         allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
#
#     @allure.story("Login Test")
#     def test_login(self, driver):
#         driver.get('http://www.demo.guru99.com/V4/')
#         driver.find_element(By.NAME, 'uid').send_keys('username')
#         driver.find_element(By.NAME, 'password').send_keys('password')
#         driver.find_element(By.NAME, 'btnLogin').click()
#
#     @allure.story("Registration Test")
#     def test_registration(self, driver):
#         driver.get('http://www.demo.guru99.com/V4/')
#         driver.find_element(By.NAME, 'username').send_keys('new_username')
#         driver.find_element(By.NAME, 'password').send_keys('new_password')
#
#         driver.find_element(By.NAME, 'submit').click()
#
#         assert "Registration success" in driver.page_source
#
#     @allure.story("Contact Us Test")
#     def test_contact_us(self, driver):
#         pass
# Файл: banking_project_test.py

import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        print(f"Unexpected alert present with text: {alert_text}")
    except NoAlertPresentException:
        pass
    finally:
        driver.close()
        driver.quit()


@allure.feature("Banking Project Tests")
class TestBankingProject:

    @pytest.fixture(autouse=True)
    def allure_attach_screenshot(self, driver, request):
        # Add code for attaching screenshots to Allure report
        yield
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.story("Login Test")
    def test_login(self, driver):
        driver.get('http://www.demo.guru99.com/V4/')
        driver.find_element(By.NAME, 'uid').send_keys('username')
        driver.find_element(By.NAME, 'password').send_keys('password')
        driver.find_element(By.NAME, 'btnLogin').click()

    @allure.story("Registration Test")
    def test_registration(self, driver):
        # Add code to test registration functionality
        pass

    @allure.story("Contact Us Test")
    def test_contact_us(self, driver):
        # Add code to test contact us functionality
        pass
