from time import sleep, time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'    # normal / методы загрузки страницы
# options.add_argument("--headless")
# options.add_argument("--disable-cache")
options.add_argument("--window-size=1920,1080")
# options.add_argument("--ignore-certificate-errors")  # игнорирования ssl сертификата
# options.add_argument("--incognito")  # позволяет не использовать кэш и сохранять данные

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# driver.set_window_size(1920, 1080)    # но браузер применят это только после инициализации в отличие от опции

start_time = time()

driver.get("https://whatismyipaddress.com/")

end_time = time()
result = end_time - start_time
print(result )