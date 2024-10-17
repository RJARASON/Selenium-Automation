def EcobankOnlineauto():
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time
        import os
        import task
        import logging

        s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        wait=WebDriverWait(driver,100)

        os.system("cls")
        driver.maximize_window()
        driver.get("https://digixuat.ecobank.com/?page=login-form")
        print("Url gotten!")
        ImageAD=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='rectangle-copy']//img")))
        gotologinbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='showLoginPage2']")))
        gotologinbtn.click()
        userinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_username|input']")))
        userinput.send_keys('gm49012645')#gm49012645
        print("username entered!")

        passwordinput=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login_password|input']")))
        print("password entered!")
        passwordinput.send_keys('Welcome@7')#Welcome@7
        loginbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Log in']")))
        loginbtn.click()
        print("login btn clicked!")
        navbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='hamburger-icon']")))
        navbtn.click()
        time.sleep(6)
        print("Nav btn clicked!")
        Accountspan=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@alt='Accounts']")))
        Accountspan.click()
        time.sleep(6)
        print("Account btn clicked!")
        MyAccountbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@alt='My Accounts']")))
        MyAccountbtn.click()
        time.sleep(6)
        print("My Account btn clicked!")
        Accountdetails=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@alt='Account Details']")))
        Accountdetails.click()
        print("My Account Details btn clicked!")
        proceedbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@data-bind='text:locale.generic.common.proceed']")))
        proceedbtn.click()
        print("Proceed btn clicked!")
        CustomerName=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='cust-name']")))
        print(f"Customer Name : {CustomerName.text}")
        AccountNumbertext=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'6240009482')]")))
        print(f"Account Number : {AccountNumbertext.text}")
        AccountBalance=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='cust-account'][normalize-space()='GMD 429,304.00']")))
        print(f"Account Balance : {AccountBalance.text}")
        time.sleep(10)
    except KeyboardInterrupt:
        task.Fin()
EcobankOnlineauto()
