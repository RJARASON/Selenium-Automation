from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sendGmail import SendEmail

s = Service('C:\\Users\Steiner Paul Tidings\\Documents\\Kodjo Messi\\Selenium-Automation-main\\Automation\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
wait = WebDriverWait(driver, 30)




def Login():
    driver.get('https://www.linkedin.com/login')
    # email_input=driver.find_element(By.ID,'session_key/')
    email_input=driver.find_element(By.ID,'username')
    email_input.send_keys("anangasher@gmail.com")
    # pass_input=driver.find_element(By.ID,'session_password')
    pass_input=driver.find_element(By.ID,'password')
    pass_input.send_keys("Chris@1038")
    # sign_btn=driver.find_element(By.XPATH,"//button[@type='submit']")
    sign_btn=driver.find_element(By.XPATH,"//button[@aria-label='Sign in']")
    sign_btn.click()
    # email_input.click()
    # pass_input.click()
    

def Search():
    # inputbox=driver.find_element(By.XPATH,"//input[@placeholder='Search']")
    inputbox=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
    inputbox=driver.find_element(By.CLASS_NAME,"search-global-typeahead__input")
    inputbox.send_keys(Keys.ADD)
    inputbox.send_keys("Steiner paul tidings")
    inputbox.send_keys(Keys.ENTER)
    inputbox.click()
    time.sleep(6)

def Viewprofile():
    # button=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='View full profile']")))
    button=driver.find_element(By.XPATH,"//*[text()='View full profile']")
    button.click()
    time.sleep(6)
    # msgbtn1=driver.find_element(By.XPATH,"//button[@id='ember189']")
    # msgbtn1.click()
    # time.sleep(6)


def messageuser():
    # msgbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.//span[text()='Message']]")))
    # msgbtn=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Message')]")))
    # msgbtn=driver.find_element(By.XPATH, "//div[.//button[contains(@aria-label, 'Message')]]")
    msgbtn=driver.find_element(By.XPATH, "")
    #sgbtn.click()
    # msgbtn=driver.find_element
    # (By.CLASS_NAME,"artdeco-button__text")
    textbox=driver.find_element(By.CLASS_NAME,"msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 full-height notranslate")
    textbox.click()
    textmsg=driver.find_element(By.XPATH,"1")
    textmsg.send_keys(Keys.ADD)
    textmsg.send_keys("Hello Paul. It's great connecting with you. How have you been?")
    textmsg.send_keys(Keys.ENTER)
    sendbtn=driver.find_element(By.ID,"ember967")
    sendbtn.click()

def LinkedIn():
    Login()
    Search()
    Viewprofile()
    # messageuser()
    SendEmail()
LinkedIn()


def Signout():
    profilebtn2=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[text()="Me"]')))
    profilebtn2.click()
    # signout=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Sign Out')]")))
    signout=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[text()="Sign Out"]')))
    # signout=driver.find_element(By.ID,'ember21')
    signout.click()
    time.sleep(30)


def SignUp():
    s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    driver.get('https://www.linkedin.com/home')

    linkbtn=driver.find_element(By.XPATH,"//a[@class='sign-in-form__join-cta link link-no-visited-state']")
    linkbtn.click()
    email=driver.find_element(By.ID,"email-address")
    email.send_keys("jakerzoly@gmail.com")
    email.click()
    password=driver.find_element(By.XPATH,"//input[@id='password']")
    password.send_keys("5802671d")
    signbtn=driver.find_element(By.XPATH,"//button[@id='join-form-submit']")
    signbtn.click()
    