from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()

#get username and password from user
username = input("Enter Email for LinkedIn: ")
password = input("Password for LinkedIn: ")

#goes to linkedin
url = "https://www.linkedin.com/"
driver = webdriver.Chrome(os.environ.get('CHROMEDRIVERPATH'))
driver.get(url)

#fill username
usernameField = driver.find_element_by_xpath('//*[@id="session_key"]')
usernameField.send_keys(username)

#fill password
passwordField = driver.find_elements_by_xpath('//*[@id="session_password"]')
passwordField[0].send_keys(password)

#login
loginButton = driver.find_element_by_class_name("sign-in-form__submit-button")
loginButton.send_keys(Keys.RETURN)