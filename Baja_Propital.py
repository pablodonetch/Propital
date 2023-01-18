import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://propital.prop360.cl/")
username = driver.find_element("id", "tbMail")
password = driver.find_element("id", "tbPassword")
username.send_keys("contacto@donetch.cl")
password.send_keys("donetch$1245")
driver.find_element("id", "botLogin").click()
time.sleep(2)
driver.get("https://propital.prop360.cl/backOffice/propiedades/propiedades.aspx?cor=1323")
for i in range(0,2):
    time.sleep(2)
    boton=driver.find_elements(By.XPATH, "//*[@class='btn btn-xs default blue-stripe lnkEdit']")
    boton[0].click()
    time.sleep(2)
    boton=driver.find_elements(By.XPATH, "//*[@class='itemMenuMax']")
    boton[4].click()
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "//*[@class='btn grey-cascade lnkPH']").click()
        time.sleep(1)
        driver.find_element("id", "butMotivoPH").click()
        # Cambiar al contexto de la alerta
        alert = driver.switch_to.alert
        # Aceptar la alerta
        alert.accept()
    except:
        pass
    time.sleep(1)#espera
    driver.get("https://propital.prop360.cl/backOffice/propiedades/propiedades.aspx?cor=1323")#vuelve a la página inicial de la cartera
