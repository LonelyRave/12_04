import pytest
from Lesson_18.tests.banking_project_test import TestBankingProject
from Lesson_18.tests.contact_us_test import TestContactUs
from Lesson_18.tests.the_internet_test import TestTheInternet


@pytest.mark.suite
def test_suite_login(driver):
    test_banking_project = TestBankingProject()
    test_banking_project.test_login(driver)


@pytest.mark.suite
def test_suite_registration(driver):
    test_banking_project = TestBankingProject()
    test_banking_project.test_registration(driver)


@pytest.mark.suite
def test_suite_contact_us(driver):
    test_contact_us = TestContactUs()
    test_contact_us.test_contact_us(driver)


@pytest.mark.suite
def test_suite_internet(driver):
    test_the_internet = TestTheInternet()
    test_the_internet.test_internet(driver)
