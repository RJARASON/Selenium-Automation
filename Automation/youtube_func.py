from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.youtube.com')
inputbox=driver.find_element(By.XPATH,"//input[@id='search']")
searchbtn=driver.find_element(By.ID,"search-icon-legacy")
vidbtn=driver.find_element(By.ID,"thumbnail-container")
inputbox.send_keys('monody the fat rat')
searchbtn.click()
vidbtn.click()
time.sleep(6)