from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')
driver.maximize_window()
page = driver.page_source
print(page)
sleep(5)
url = driver.current_url
title = driver.title

assert url == 'https://google22.com', 'ошибка в url'
assert title == 'google', 'ошибка в title'

print(url, title)