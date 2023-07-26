import pytest

from utils.test_config import TestConfig

print ( TestConfig.HOST )  # Выведет "https://demoqa.com/"
print ( TestConfig.ALLURE_RESULTS_DIR )  # Выведет "./allure-results/"

if __name__ == "__main__" :
    pytest.main ( )
