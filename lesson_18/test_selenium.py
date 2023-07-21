import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.selenium
def test_search(browser):
    browser.get("https://www.example.com")

    assert search_results_found(), "Результаты поиска не найдены"


@pytest.mark.selenium
def test_navigation(browser):
    browser.get("https://www.example.com")

    assert navigation_successful(), "Навигация не выполнена"
