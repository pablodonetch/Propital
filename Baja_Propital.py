import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://propital.prop360.cl/")
username = driver.find_element("id", "tbMail")
password = driver.find_element("id", "tbPassword")
username.send_keys("contacto@donetch.cl")
password.send_keys("donetch$1245")
driver.find_element("id", "botLogin").click()
time.sleep(5)