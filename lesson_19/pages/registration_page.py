from selenium.webdriver.common.by import By

from lesson_19.pages.base_page import BasePage


class RegistrationPage ( BasePage ) :
    URL = "https://demoqa.com/register"

    def open(self) :
        self.driver.get ( self.URL )

    def register(self , username , password , email) :
        self.enter_text ( (By.ID , "userName") , username )
        self.enter_text ( (By.ID , "password") , password )
        self.enter_text ( (By.ID , "email") , email )
        self.click_element ( (By.ID , "register") )
