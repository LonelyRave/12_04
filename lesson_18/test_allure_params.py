import allure
import pytest


def login_successful(username, password):
    users = {
        "user1": "password1",
        "user2": "password2",
    }

    if username in users and users[username] == password:
        return True
    else:
        return False


@pytest.mark.allure
@pytest.mark.parametrize("username, password", [("user1", "password1"), ("user2", "password2")])
def test_login(username, password):
    with allure.step("Шаг 1: Ввод логина"):
        allure.attach("Введенный логин", username)

    with allure.step("Шаг 2: Ввод пароля"):
        allure.attach("Введенный пароль", password)

    with allure.step("Шаг 3: Нажатие кнопки Войти"):

    with allure.step("Шаг 4: Проверка успешного входа"):
        assert login_successful(), "Вход выполнен"

    with allure.step("Шаг 5: Отображение информации о пользователе"):


@pytest.mark.smoke
def test_smoke_test():
    with allure.step("Step 1: Perform a simple action"):
        print("Performing a simple action...")
    with allure.step("Step 2: Check the result"):
        print("Checking the result...")
        assert True, "Test Failed!"
