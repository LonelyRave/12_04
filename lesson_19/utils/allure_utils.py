import os

import allure
from utils.test_config import TestConfig


class Allure :

    @staticmethod
    def attach_screenshot(driver , name) :
        allure_dir = TestConfig.ALLURE_RESULTS_DIR
        allure.attach ( driver.get_screenshot_as_png ( ) , name=name , attachment_type=allure.attachment_type.PNG )


def set_up() :
    allure_dir = TestConfig.ALLURE_RESULTS_DIR
    if not os.path.exists ( allure_dir ) :
        os.makedirs ( allure_dir )
    allure.environment ( host=TestConfig.HOST )
