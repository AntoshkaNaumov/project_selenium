from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from auth_data import instagram_password, instagram_login
from selenium.webdriver.chrome.service import Service


# options
options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0")

s = Service("C:\\Users\\79633\\PycharmProjects\\selenium\\firefoxdriver\\geckodriver.exe")
driver = webdriver.Firefox(service=s, options=options)

try:
    driver.get("https://www.instagram.com/")
    time.sleep(5)
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(instagram_login)
    time.sleep(5)
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(instagram_password)
    time.sleep(5)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
