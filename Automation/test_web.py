def Click_button_DL():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    import time


    s = Service('C:\\Users\\Emmanuel and Selom\\Documents\\Brightchamps\\vsc s\\chromedriver-win32\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    driver.get("file:///C:/Users/Emmanuel%20and%20Selom/Documents/Brightchamps/vsc%20s/HTML/Driving%20license/DL.html")
    button=driver.find_element(By.ID,"Home")
    button.click()
    time.sleep(3)
    driver.back()
    button=driver.find_element(By.ID,"create")
    button.click()
    time.sleep(4)
    driver.back()
    time.sleep(3)
    driver.back()
    button=driver.find_element(By.ID,"create")
    button.click()
    Fnameinput=driver.find_element(By.ID,"Fname")
    Fnameinput.send_keys("Kodjo")

    Lnameinput=driver.find_element(By.ID,"Lname")
    Lnameinput.send_keys("Messie")

    dateb=driver.find_element(By.ID,"dateofB")
    dateb.send_keys("05/07/2007")

    Tel=driver.find_element(By.ID,"Tel")
    Tel.send_keys("0557968414")

    emaili=driver.find_element(By.ID,"email")
    emaili.send_keys("kodjomessie@gmail.com")

    addr=driver.find_element(By.ID,"address")
    addr.send_keys("Asene street 35 New Achimota")

    Dropdown1=driver.find_element(By.ID,"dropdown")
    Dropdown1.click()

    button1=driver.find_element(By.ID,"license_p1")
    button1.click()

    Dropdown2=driver.find_element(By.ID,"Dropdown")
    button2=driver.find_element(By.ID,"p1")
    button2.click()
    
    time.sleep(5)
    Subbutton=driver.find_element(By.ID,"Submit")
    Subbutton.click()
    time.sleep(5)