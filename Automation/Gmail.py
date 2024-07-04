from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
def Start_Session():
    """Function to Login into a Gmail Account"""

    s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)        
    def Gmail_login():
        driver.get('https://google.com')
        button=driver.find_element(By.LINK_TEXT,"https://mail.google.com/mail/?tab=rm&ogbl")
        button.click()

        button=driver.find_element(By.XPATH,"//a[@data-action='sign in']")
        button.click()
        
        email_input=driver.find_element(By.ID,"identifierId")
        email_input.send_keys('kodjomessieie@gmail.com')
        email_input.send_keys(Keys.ENTER)
        # button=driver.find_element(By.XPATH,"(//button[@jsname='LgbsSe'])[2]")
        # button.click()
        time.sleep(20)
        password_input=driver.find_element(By.XPATH,"(//input[@jsname='YPqjbf'])[1]")#//input[@type='password']
        password_input.send_keys("945295KODJO@")
        password_input.send_keys(Keys.ENTER)

        button=driver.find_element(By.NAME,"Next")
        button.click()

        

    Gmail_login()

def Create_Account():
    service=Service('C:\\Users\\Emmanuel and Selom\\Documents\\Brightchamps\\vsc s\\chromedriver-win32\\chromedriver.exe')
    driver=webdriver.Chrome(service=service)
    driver.get('https://google.com')
    button=driver.find_element(By.XPATH,"//a[@href='https://mail.google.com/mail/&ogbl']")
    button.click()

    button=driver.find_element(By.XPATH,"//a[@data-action='sign in']")
    button.click()
    # email_input=driver.find_element(By.ID,"identifierId")
    # email_input.send_keys('kodjomessie@gmail.com')

    button=driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
    button.click()

Start_Session()