def Searchwiki(searchtext):
    try:
        from selenium.webdriver.common.by import By
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import os
        import requests

        requests.get("https://www.wikipedia.org/",timeout=5)
        s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        wait=WebDriverWait(driver,100)

        driver.maximize_window()
        driver.get("https://www.wikipedia.org/")
        print("Browser started!")
        searchbar=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='searchInput']")))
        searchbar.send_keys(searchtext,Keys.ENTER)
        para=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[2]")))
        searchfile=open('WikiSearch/Searches.txt','a')
        os.system("cls")
        searchfile.write(f"\n\n{para.text}\n\n")
        print(para.text)
        print("Content written to file!".upper())
    except requests.ConnectionError:
        os.system("cls")
        print("INTERNET DISCONNECTED")
    except TimeoutError:
        os.system("cls")
        print("Internet is slow or page took too long to load")

Searchwiki("MacBook Pro")



