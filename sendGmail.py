from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

s = Service('C:\\Users\Steiner Paul Tidings\\Documents\\Kodjo Messi\\Selenium-Automation-main\\Automation\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
wait = WebDriverWait(driver, 30)


def SendEmail():
    driver.get('https://mail.google.com/mail/?view=cm&fs=1&tf=1')
    inputbox1=driver.find_element(By.ID,":rx")
    inputbox1.send_keys("adjeisteiner@gmail.com")
    inputbox2=driver.find_element(By.ID,":oo")
    inputbox2.send_keys("Kodjo Messie")
    inputbox3=driver.find_element(By.ID,":ne")
    inputbox3.send_keys("Hi Paul. Just wanted to drop a quick note to say hello. Hope you're having a great day!")
    sendbtn=driver.find_element(By.ID,":oy")
    sendbtn.click()

SendEmail()    
