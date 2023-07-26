import pytest
from pages.home_page import HomePage
from selenium import webdriver
from utils.allure import Allure


@pytest.fixture ( scope="module" )
def browser() :
    driver = webdriver.Chrome ( )
    yield driver
    driver.quit ( )


@pytest.fixture ( autouse=True )
def allure_setup(request) :
    Allure.set_up ( )


def test_home_page_title(browser) :
    home_page = HomePage ( browser )
    home_page.open ( )
    assert home_page.get_title ( ) == "ToolsQA"
    Allure.attach_screenshot ( browser , "Home page" )
