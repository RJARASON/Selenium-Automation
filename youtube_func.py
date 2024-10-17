from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service=Service('C:\\Users\\Emmanuel and Selom\\Documents\\Brightchamps\\vsc s\\chromedriver-win32\\chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get('https://www.youtube.com')
inputbox=driver.find_element(By.ID,"search")
inputbox.send_keys('the fat rat')
inputbox.click()
