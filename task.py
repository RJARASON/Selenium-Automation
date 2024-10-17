from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os
import pyautogui
import time
import logging

def Error_Unlocatelement():
    os.system("cls")
    print(f"Selenium is unable to locate element")


def LoginEcobankOnline():
    s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    wait=WebDriverWait(driver,30)

    driver.maximize_window()
    driver.get("https://digixuat.ecobank.com/?page=login-form")
    time.sleep(20)
    ImageAD=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='rectangle-copy']//img")))
    gotologinbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='showLoginPage2']")))
    gotologinbtn.click()
    userinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_username|input']")))
    userinput.send_keys('gm49012645')

    passwordinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_password|input']")))
    passwordinput.send_keys('Welcome@7')

    loginbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Log in']")))
    loginbtn.click()

def GetCursorpos():
    time.sleep(3)
    print(pyautogui.position())

def Fin():
    os.system("cls")
    print("AUTOMATION INTERRUPTED!")  

def WebInfo():
    s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    wait=WebDriverWait(driver,30)

    website= driver.title
    url=driver.current_url
    orientation=driver.orientation
    pagesource=driver.page_source
    windowshandle=driver.current_window_handle
    print("=================================")
    print(f"Website title : {website}")
    print(f"Url : {url}")
    print(f"Orientation : {orientation}")
    print(f"Page Source : {pagesource}")
    print(f"Windows Handle : {windowshandle}")
    print("=================================")