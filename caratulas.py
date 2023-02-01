import time, math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
inicio= 20146000
final = 20150800
driver.get("https://conservador.cl/portal/estado?caratula=20120608")

username = driver.find_element("id", "caratula")
