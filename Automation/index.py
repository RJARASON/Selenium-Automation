from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Locate chromedriver to automate
s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver.exe')

# set up a Selenium WebDriver for Chrome, 
# which is necessary for automating web browser interactions in Python
driver = webdriver.Chrome(service=s)

# Get google page
driver.get('https://google.com')
# Get google title
title=driver.title()
# print google title
print(title)