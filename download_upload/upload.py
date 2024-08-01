from time import sleep, time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

downloads_path = os.path.join(os.getcwd(), 'downloads', 'test_cypress.png')
# print(downloads_path)
# sleep(1000)

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://the-internet.herokuapp.com/upload')

sleep(3)
upload_file = driver.find_element('xpath', '//input[@type="file"]')
# вместо input может быть button и в нем уже есть input который не видим в структуре html //input[@type='file']
upload_file.send_keys(f"{downloads_path}")
sleep(100)