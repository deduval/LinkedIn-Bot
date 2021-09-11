from selenium import webdriver
import os
from dotenv import load_dotenv
import time

load_dotenv()

url = "https://www.linkedin.com/"
driver = webdriver.Chrome(os.environ.get('CHROMEDRIVERPATH'))
driver.get(url)

print(driver.title)
time.sleep(5)

driver.quit()