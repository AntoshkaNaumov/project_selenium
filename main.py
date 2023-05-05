from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from fake_useragent import UserAgent


# url = "https://www.instagram.com/"

user_agent_list = [
    "hello_world",
    "best_of_the_best",
    "python_today"
]

useragent = UserAgent()

# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld:)")
# options.add_argument(f"user-agent={random.choice(user_agent_list)}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy
# options.add_argument("--proxy-server=138.128.91.65:8000")


s = Service("C:\\Users\\79633\\PycharmProjects\\selenium\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    # time.sleep(5)
    # driver.get('https://stackoverflow.com/')
    # time.sleep(5)
    # driver.refresh()
    # time.sleep(2)
    # driver.get_screenshot_as_file('1.png')
    # driver.save_screenshot('2.png')
    # time.sleep(2)
    driver.get("https://2ip.ru")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
