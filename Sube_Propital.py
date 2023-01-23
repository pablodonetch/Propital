import time, math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://propital.prop360.cl/")
username = driver.find_element("id", "tbMail")
password = driver.find_element("id", "tbPassword")
username.send_keys("contacto@donetch.cl")
password.send_keys("donetch$1245")
driver.find_element("id", "botLogin").click()
time.sleep(2)
hay=1
while hay==1:
    driver.get("https://propital.prop360.cl/backOffice/propiedades/propiedades.aspx?cor=1323")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@class='btn btn-circle blue-hoki tuto tuto_ml']").click()
    time.sleep(1)
    #borra "activa" y escribe "pasiva"
    password = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='s2id_autogen3']")))
    password.click()
    password.send_keys(Keys.BACKSPACE)
    password.send_keys(Keys.BACKSPACE)
    password.send_keys('Pasiva')
    password.send_keys(Keys.ENTER)
    time.sleep(2)
    #hace click en boton azul
    driver.find_element("id", "butActionFilter").click()
    time.sleep(2)
    try:
        # busca el botón para editar
        boton=driver.find_elements(By.XPATH, "//*[@class='btn btn-xs default blue-stripe lnkEdit']")
        boton[0].click()
        time.sleep(2)
        boton=driver.find_elements(By.XPATH, "//*[@class='itemMenuMax']")
        boton[4].click()
        time.sleep(1)
        botonverde=driver.find_element(By.XPATH, "//*[@class='btn green']")
        botonverde.click()
        # Cambiar al contexto de la alerta
        alert = driver.switch_to.alert
        # Aceptar la alerta
        alert.accept()
        time.sleep(2)
    except:
        hay=0

hay=1
while hay==1:
    driver.get("https://propital.prop360.cl/backOffice/propiedades/propiedades.aspx?cor=1323")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@class='btn btn-circle blue-hoki tuto tuto_ml']").click()
    time.sleep(1)
    #borra "activa" y escribe "pasiva"
    password = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='s2id_autogen3']")))
    password.click()
    password.send_keys(Keys.BACKSPACE)
    password.send_keys(Keys.BACKSPACE)
    password.send_keys('No Disponible')
    password.send_keys(Keys.ENTER)
    time.sleep(2)
    #hace click en boton azul
    driver.find_element("id", "butActionFilter").click()
    time.sleep(2)
    try:
        # busca el botón para editar
        boton=driver.find_elements(By.XPATH, "//*[@class='btn btn-xs default blue-stripe lnkEdit']")
        boton[0].click()
        time.sleep(2)
        boton=driver.find_elements(By.XPATH, "//*[@class='itemMenuMax']")
        boton[4].click()
        time.sleep(1)
        comision = driver.find_element("id", "tbComision1")
        comision.send_keys("2")
        driver.find_element("id", "botGrabarDatos_f2").click()
        time.sleep(2)
        driver.find_element("id", "lnk_ND_PVC_f2").click()
        time.sleep(2)
        # Cambiar al contexto de la alerta
        alert = driver.switch_to.alert
        # Aceptar la alerta
        alert.accept()
        time.sleep(2)
    except:
        hay=0