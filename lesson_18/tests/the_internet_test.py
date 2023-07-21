import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


class TestTheInternet:

    @pytest.fixture(autouse=True)
    def allure_attach_screenshot(self, driver, request):
        pass

    @allure.feature("The Internet Website")
    @allure.story("Login Test")
    def test_login(self, driver):
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Form Authentication').click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.feature("The Internet Website")
    @allure.story("Some Other Test")
    def test_some_other_test(self, driver):
        pass
