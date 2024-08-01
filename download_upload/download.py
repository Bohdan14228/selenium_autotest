from time import sleep, time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

# указываем путь к дефолтной папке
downloads_path = os.path.join(os.getcwd(), 'downloads')
prefs = {
    "download.default_directory": f"{downloads_path}"
}
options.add_experimental_option("prefs", prefs)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://the-internet.herokuapp.com/download')

sleep(3)
driver.find_elements('xpath', '//a')[3].click()
sleep(100)