from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import requests

s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
wait=WebDriverWait(driver,100)
def USER_ACCESS_AND_LOGIN_FOR_AN_EXISTING_CUSTOMER():
    try:
        requests.get("https://digixuat.ecobank.com/?page=login-form",timeout=5)

        def geturl():
            driver.get("https://digixuat.ecobank.com/?page=login-form")
            ImageAD=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='rectangle-copy']//img")))
            gotologinbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='showLoginPage2']")))
            gotologinbtn.click()

        def test_with_blank_password():    
            geturl()
            userinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_username|input']")))
            userinput.send_keys('gm49012645')
            passwordinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_password|input']")))
            passwordinput.send_keys('')#Welcome@7
            print("TEST FOR LOGIN USING VALID AFFILIATE,VALID USERNAME, BLANK PASSWORD | THE CUSTOMER SHOULD BE PROMPTED THAT THE LOG IN THE DETAILS CANNOT BE BLANK/ INVALID.")
            driver.close()

        def Test_that_customer_can_click_on_view_password():
            geturl()
            viewcon=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@id='eyecon']")))
            viewcon.click()
            print("Test that customer can click on view password icon to display valid password	 | Customer should be able to view password")
            driver.close()

        def test_that_customer_can_select_languages():
            geturl()
            dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='oj-button-icon oj-end oj-component-icon oj-button-menu-dropdown-icon']")))
            dropdown.click()
            print("Test that the customer can select any of the following languages in the drop down displayed in alphabetical order.: -English -French -Portuguese -Spanish | The customer should be able to select language displayed in alphabetical order. and change language successfully")
            driver.close()

        def test_that_customer_selects_English():                                         
            geturl()
            dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='oj-button-icon oj-end oj-component-icon oj-button-menu-dropdown-icon']")))
            dropdown.click()
            english=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@data-bind='text:$data.description'][normalize-space()='English']")))
            english.click()
            print("Test that when the customer selects English, subsequent pages are translated and/to displayed in English | All pages should be displayed in English")
            driver.close()

        def test_that_customer_selects_French():
            geturl()
            dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='oj-button-icon oj-end oj-component-icon oj-button-menu-dropdown-icon']")))
            dropdown.click()
            french=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Français']")))
            french.click()
            print("Test that when the customer selects French, subsequent pages are translated and/to displayed in French| All pages should be displayed in French")
            driver.close()

        def test_that_customer_selects_Spanish():
            geturl()
            dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='oj-button-icon oj-end oj-component-icon oj-button-menu-dropdown-icon']")))
            dropdown.click()
            Spanish=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Spanish']")))
            Spanish.click()
            print("Test that when the customer selects Spanish, subsequent pages are translated and/to displayed in Spanish	| All pages should be displayed in Spanish")
            driver.close()

        def test_that_customer_selects_Portuguese():
            geturl()
            dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='oj-button-icon oj-end oj-component-icon oj-button-menu-dropdown-icon']")))
            dropdown.click()
            Portuguese=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Portuguese']")))
            Portuguese.click()
            print("Test that when the customer selects Portuguese, subsequent pages are translated and/to displayed in Portuguese| All pages should be displayed in Portuguese")
            driver.close()

        def Test_for_customer_username_input():
            geturl()
            userinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_username|input']")))
            userinput.send_keys('gm49012645')
            print("Test for customer username input	| The customer should be able to enter a customer username for login")
            driver.close()

        def test_for_login_using_invalid_username_invalid_password():
            geturl()
            userinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_username|input']")))
            userinput.send_keys('gwrgwvw')
            passwordinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_password|input']")))
            passwordinput.send_keys('46846464')
            print("Test for login using - Invalid Affiliate - Invalid username - Invalid Password| The customer should be prompted that the log in details are invalid")
            driver.close()

        def test_for_login_blank_email_Vaild_password():
            geturl()
            userinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_username|input']")))
            userinput.send_keys('gm49012645')
            passwordinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_password|input']")))
            passwordinput.send_keys('Welcome@7')
            print("Test for login using - Invalid Affiliate - Invalid customername - Valid Password	| The customer should be prompted that the log in details are invalid")
            driver.close()

        def test_for_login_Valid_Affiliate_Blank_Email_Valid_Password():
            geturl()
            userinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_username|input']")))
            userinput.send_keys('')
            passwordinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_password|input']")))
            passwordinput.send_keys('Welcome@7')
            print("Test for login using: -Valid Affiliate -Blank Email -Valid Password	| The customer should be prompted that the log in details cannot be blank / invalid")
            driver.close()

        def Test_for_login_using_Valid_Affiliate_Valid_Email_Valid_Password():
            geturl()
            userinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_username|input']")))
            userinput.send_keys('gm49012645')
            passwordinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_password|input']")))
            passwordinput.send_keys('Welcome@7')
            print("Test for login using: -Valid Affiliate -Valid Email -Valid Password	| Log in should be successful and the The customer should be navigated to the Dashboard.")
            driver.close()

        def test_that_customer_can_click_view_password_to_hide_password():
            geturl()
            viewcon=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@id='eyecon']")))
            viewcon.click()
            print("Test that customer can click on view password icon to hide password	| Customer should be able to hide password	")
            driver.close()

        def Test_customer_is_able_to_see_and_select_affiliate_on_the_navbar():
            geturl()
            viewcon=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@id='eyecon']")))
            viewcon.click()
            print("Test customer is able to see and select affiliate on the navbar	| Customer should be able to see and select affiliate, this should be displayed in alphabetical order.")
            driver.close()

        def testcases():
            test_with_blank_password()
            Test_that_customer_can_click_on_view_password()
            Test_for_customer_username_input()
            Test_for_login_using_Valid_Affiliate_Valid_Email_Valid_Password()
            test_with_blank_password()
            test_that_customer_selects_Spanish()
            test_that_customer_selects_Portuguese()
            test_that_customer_selects_French() 
            test_that_customer_selects_English()
            test_that_customer_can_select_languages()
            test_for_login_Valid_Affiliate_Blank_Email_Valid_Password()
            test_for_login_using_invalid_username_invalid_password()
            test_for_login_blank_email_Vaild_password()
            test_that_customer_can_click_view_password_to_hide_password()
            Test_customer_is_able_to_see_and_select_affiliate_on_the_navbar()
        testcases()

    except TimeoutError:
        print("Internet is slow or page took too long to respond".upper())



def FORGOTTEN_PASSWORD():
    def geturl():
        driver.get("https://digixuat.ecobank.com/?page=login-form")
        ImageAD=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='rectangle-copy']//img")))
        gotologinbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='showLoginPage2']")))
        gotologinbtn.click()
    
    def test_that_customer_can_submit_valid_customer_details():    
        geturl()
        forgotpasswordbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Forgot Password?']")))
        forgotpasswordbtn.click()
        accouninput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='accNo|input']")))
        accouninput.send_keys("6240009482",Keys.ENTER)
        submitbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//oj-button[@class='action-button-primary oj-button oj-button-full-chrome oj-button-text-only oj-enabled oj-complete oj-default']//div[@class='oj-button-label']")))
        submitbtn.click()
        print("test_that_customer_can_submit_valid_customer_details".upper())
        driver.close()
        