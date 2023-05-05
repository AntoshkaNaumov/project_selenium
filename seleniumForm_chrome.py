from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from auth_data import vk_password

from selenium.webdriver.common.by import By

# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

s = Service("C:\\Users\\79633\\PycharmProjects\\selenium\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get("https://vk.com")
    time.sleep(5)
    email_input = driver.find_element(By.ID, "index_email")
    email_input.send_keys("79633045137")
    time.sleep(5)
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)
    login_button = driver.find_element(By.CSS_SELECTOR, "[class='vkc__PureButton__button vkc__Link__link vkc__Link__primary vkc__Bottom__switchToPassword']").click()
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(vk_password)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
