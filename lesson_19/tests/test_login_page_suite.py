import allure


@allure.feature ( "Тестування сторінки логіну" )
class TestLoginPage :

    @allure.title ( "Перевірка переходу на сторінку логіну" )
    def test_login(self , home_page , login_page) :
        home_page.open ( )
        home_page.click_login_button ( )

        assert login_page.is_login_page ( )

        login_page.enter_username ( "testuser" )
        login_page.enter_password ( "testpass" )
        login_page.click_login_button ( )

        assert login_page.is_user_logged_in ( )

        login_page.click_logout_button ( )

        assert login_page.is_user_logged_out ( )
