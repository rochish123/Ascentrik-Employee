import time
import mat as mat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.get("http://104.211.153.80:8080/")
driver.maximize_window()

driver.find_element(By.NAME,"username").send_keys("sadmin")
driver.find_element(By.NAME,"password").send_keys("AscentrikCXL#19")
driver.find_element(By.XPATH,"/html/body/app-root/s-login-pg/html/body/div/div/div/div/div[1]/div/div[2]/div[1]/div/footer/button").click()

