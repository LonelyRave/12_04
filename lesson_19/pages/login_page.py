from selenium.webdriver.common.by import By

from lesson_19.pages.base_page import BasePage


class LoginPage ( BasePage ) :
    URL = "https://demoqa.com/login"

    def open(self) :
        self.driver.get ( self.URL )

    def login(self , username , password) :
        self.enter_text ( (By.ID , "username") , username )
        self.enter_text ( (By.ID , "password") , password )
        self.click_element ( (By.ID , "login") )
