import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def chrome_driver():
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service)

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture(autouse=True)
def allure_attach_screenshot(request, chrome_driver):
    yield

    if request.node.rep_call.failed:
        allure.attach(chrome_driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
