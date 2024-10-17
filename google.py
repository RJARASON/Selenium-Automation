import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://google.com")
Input=driver.find_element(By.ID,"APjFqb")
Input.send_keys("Microsoft Copilot")
print(Input.text)