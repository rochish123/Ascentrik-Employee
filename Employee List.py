import time
import mat as mat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.get("http://104.211.153.80:8080/")
driver.maximize_window()
#Enter UserName
driver.find_element(By.NAME,"username").send_keys("sadmin")
# enter password
driver.find_element(By.NAME,"password").send_keys("AscentrikCXL#19")
# Click Login Button
driver.find_element(By.XPATH,"/html/body/app-root/s-login-pg/html/body/div/div/div/div/div[1]/div/div[2]/div[1]/div/footer/button").click()
# act_title=driver.title
# exp_title="Ascentrik Research Pvt Ltd"
#
# if act_title==exp_title:
#     print("Login test passed")
#     print(act_title)
# else:
#     print("Login Test Failed")
time.sleep(2)
#open Menubar
driver.find_element(By.CSS_SELECTOR,"body > app-root > app-home-comp > div > mat-sidenav-container > mat-sidenav-content > nav > div:nth-child(1) > mat-toolbar > button").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/app-root/app-home-comp/div/mat-sidenav-container/mat-sidenav/div/div/perfect-scrollbar/div/div[1]/div[3]/app-side-menu-item/div/mat-accordion/mat-expansion-panel/mat-expansion-panel-header/span[1]/mat-panel-title/span[2]").click()
time.sleep(2)
# Click Employee
driver.find_element(By.XPATH,'/html/body/app-root/app-home-comp/div/mat-sidenav-container/mat-sidenav/div/div/perfect-scrollbar/div/div[1]/div[3]/app-side-menu-item/div/mat-accordion/mat-expansion-panel/div/div/div[2]/app-side-menu-item/div/a/span[1]/span[2]').click()
time.sleep(2)
# Click List
driver.find_element(By.LINK_TEXT,'List').click()
# time.sleep(2)
# minimise 
driver.find_element(By.CLASS_NAME,'header-nav').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="no-more-tables"]/table/tbody/tr[1]/td[5]/div/a[2]/i').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'#no-more-tables > table > tbody > tr:nth-child(1) > td:nth-child(1) > a').click()