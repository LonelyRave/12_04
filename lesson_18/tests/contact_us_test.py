import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


class TestContactUs:

    @pytest.fixture(autouse=True)
    def allure_attach_screenshot(self, request):
        yield
        driver = request.node.cls.driver
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.story("Homepage Test")
    def test_homepage(self, driver):
        driver.get("http://uitestingplayground.com/home")

    @allure.story("Contact Us Form Submission Test")
    def test_contact_form_submission(self, driver):
        driver.get("https://www.globalsqa.com/contact-us/")

        name_input = driver.find_element(By.ID, "comment_name")
        name_input.send_keys("John Doe")

        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("johndoe@example.com")

        subject_input = driver.find_element(By.ID, "subject")
        subject_input.send_keys("Regarding Inquiry")

        message_input = driver.find_element(By.ID, "comment")
        message_input.send_keys("Hello, I have a question.")

        captcha_image = driver.find_element(By.XPATH, "//div[@class='g-recaptcha']/div/div/iframe")
        captcha_image_url = captcha_image.get_attribute("src")
        response = requests.get(captcha_image_url)
        with open("captcha.png", "wb") as f:
            f.write(response.content)
        time.sleep(90)
