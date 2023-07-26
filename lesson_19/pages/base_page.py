from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage :
    def __init__(self , driver) :
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
