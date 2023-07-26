import pytest
from pages.registration_page import RegistrationPage
from selenium import webdriver


@pytest.fixture ( scope="module" )
def browser() :
    driver = webdriver.Chrome ( )
    yield driver
    driver.quit ( )


@pytest.fixture ( autouse=True )
def allure_setup(request) :
    set_up ( )


def test_successful_registration(browser) :
    registration_page = RegistrationPage ( browser )
    registration_page.open ( )
    registration_page.register ( "user123" , "password123" , "user123@example.com" )

    pass


def test_registration_with_existing_email(browser) :
    registration_page = RegistrationPage ( browser )
    registration_page.open ( )
    registration_page.register ( "user456" , "password456" , "existing_user@example.com" )

    pass
