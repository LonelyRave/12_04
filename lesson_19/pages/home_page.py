from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from lesson_19.pages.base_page import BasePage


class HomePage ( BasePage ) :
    URL = "https://demoqa.com/"

    def open(self) :
        self.driver.get ( self.URL )

    def get_title(self) :
        return self.driver.title

    def click_login_button(self) :
        login_button_locator = (By.ID , "login-button")
        self.click_element ( login_button_locator )


class BasePage :
    def __init__(self , driver: WebDriver) :
        self.driver = driver

    def find_element(self , locator , timeout=40) :
        try :
            element = WebDriverWait ( self.driver , timeout ).until (
                ec.presence_of_element_located ( locator )
            )
            return element
        except TimeoutException :
            raise TimeoutException ( f"Element with locator {locator} not found within {timeout} seconds." )

    def click_element(self , locator , timeout=40) :
        element = self.find_element ( locator , timeout )
        element.click ( )

    def enter_text(self , locator , text , timeout=40) :
        element = self.find_element ( locator , timeout )
        element.clear ( )
        element.send_keys ( text )
