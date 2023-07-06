import unittest

from tests.banking_project_test import BankingProjectTest
from tests.contact_us_test import ContactUsTest
from tests.the_internet_test import TheInternetTest

# Создание тест-сьюта
test_suite = unittest.TestSuite()

# Добавление тест-кейсов в тест-сьют
test_suite.addTest(unittest.makeSuite(BankingProjectTest))
test_suite.addTest(unittest.makeSuite(ContactUsTest))
test_suite.addTest(unittest.makeSuite(TheInternetTest))

# Запуск тест-сьюта
runner = unittest.TextTestRunner()
runner.run(test_suite)
