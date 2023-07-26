import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture ( scope="module" )
def browser() :
    chrome_options = Options ( )

    driver = webdriver.Chrome ( options=chrome_options )

    yield driver

    driver.quit ( )


@pytest.fixture ( autouse=True )
def allure_setup(request) :
    allure_dir = os.path.join ( os.getcwd ( ) , "allure-results" )
    if not os.path.exists ( allure_dir ) :
        os.makedirs ( allure_dir )

    allure.environment ( host="https://demoqa.com/" )


def pytest_html_report_title(report) :
    report.title = "Тестовий звіт"


@pytest.fixture ( scope="module" )
def home_page(browser) :
    return HomePage ( browser )


@pytest.fixture ( scope="module" )
def login_page(browser) :
    return LoginPage ( browser )


@pytest.fixture ( scope="module" )
def registration_page(browser) :
    return RegistrationPage ( browser )
