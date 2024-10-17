from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

s=Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe')
driver=webdriver.Chrome(service=s)
wait=WebDriverWait(driver,100)

driver.get("file:///C://Users/MESSIE/Documents/Websites/Delkon/Delkon%20Website.html")
driver.maximize_window()
nav1btn=wait.until(EC.element_to_be_clickable((By.ID,"nav1")))
nav1btn.click()
imagebtn=wait.until(EC.element_to_be_clickable((By.ID,"img1")))
imagebtn.click()
lunchbtn=wait.until(EC.element_to_be_clickable((By.ID,"btn1")))
lunchbtn.click()
time.sleep(5)
driver.back()
dinbtn=wait.until(EC.element_to_be_clickable((By.ID,"btn2")))
dinbtn.click()
time.sleep(5)
driver.back()
desbtn=wait.until(EC.element_to_be_clickable((By.ID,"btn3")))
desbtn.click()
time.sleep(5)
driver.back()
driver.execute_script('alert("finished clicking all three buttons!")')
time.sleep(2)
driver.quit()

