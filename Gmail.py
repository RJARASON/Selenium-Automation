from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import task

GMAIL_LOGIN_URL="https://accounts.google.com/v3/signin/identifier?ifkv=ARpgrqdLYt1CBDMrlAXRBx5mS7wVQzlEBdphibeFs2JVI0aeZepGmbOhLT49KTh1xapNk7yoEmzdhg&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1257428243%3A1727812315916024&ddm=0"
s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=s)
wait=WebDriverWait(driver,100)

driver.maximize_window()
driver.get(GMAIL_LOGIN_URL)
email_input=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='identifierId']")))
email_input.send_keys('kodjomessie@gmail.com')

nextbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Next']")))
nextbtn.click()

# password_input=driver.find_element(By.XPATH,"(//input[@jsname='YPqjbf'])[1]")#//input[@type='password']
# password_input.send_keys("945295KODJO@")
# password_input.send_keys(Keys.ENTER)

