from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')
sleep(10)
# driver.back()   # возврат назад
# driver.forward()  # возврат вперед
driver.refresh()  # перезагрузка
sleep(2)
