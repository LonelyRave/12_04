import allure
import pytest


def login_successful():
    return True


def logout_successful():
    return True


@pytest.mark.allure
def test_allure_step1():
    with allure.step("Шаг 1: Переход на сайт"):
        print("Переход на сайт...")
    with allure.step("Шаг 2: Проверка успешного входа"):
        print("Проверка успешного входа...")
        assert True, "Test Failed!"


@pytest.mark.allure
def test_logout():
    with allure.step("Шаг 1: Выход из аккаунта"):
        print("Выход из аккаунта...")

    with allure.step("Шаг 2: Проверка успешного выхода"):
        assert logout_successful(), "Выход не выполнен"


@allure.story('My first story')
class TestAllure:

    @allure.title('Test something')
    def test_something(self):
        with allure.step('Step 1: Perform some action'):
            print("Выполняем действие...")
            pass

        with allure.step('Step 2: Verify the result'):
            assert True

    @allure.title('Test another thing')
    @allure.description('This is a test for another thing')
    def test_another_thing(self):
        with allure.step('Step 1: Perform some action'):
            print("Выполняем другое действие...")
            pass

        with allure.step('Step 2: Verify the result'):
            assert False
