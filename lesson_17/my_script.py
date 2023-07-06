from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Создаю экземпляр драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))

# Открываю первую ссылку
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
print("Title 1:", driver.title)

# Открываю вторую ссылку
driver.get("http://uitestingplayground.com/home")
print("Title 2:", driver.title)

# Открываю третью ссылку
driver.get("http://the-internet.herokuapp.com/")
print("Title 3:", driver.title)

# Закрываю браузер
driver.quit()
