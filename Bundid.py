def BundIDAutoGetText():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    import os
    import sys
    import requests


    try:
        requests.get("https://bund-a.pre.buergerserviceportal.de/de",timeout=5)


        chromedriverpath={
            "Kodjo":"C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe",
            "Patrick":"c:\\phyton_automation\\Webdrivers\\chromedriver.exe"
        }


        s = Service(chromedriverpath["Kodjo"]) 
        driver = webdriver.Chrome(service=s)
        wait=WebDriverWait(driver,500)
        
        driver.maximize_window()
        driver.get("https://bund-a.pre.buergerserviceportal.de/de")
        language=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Deutsch']")))
        language.click()
        english=wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='English']")))
        english.click()
        Linkbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='All useful information']")))
        Linkbtn.click()
        os.system("cls")

        # what is bundid dropdown
        dropdown1=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[1]/div[2]/button[1]")))
        dropdown1.click()
        dropdown1text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'BundID is a central account which you can use to p')]")))
        dropdown1text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'All communications related to your online request ')]")))
        dropdown1text3=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'For quick and easy access to your online requests ')]")))
        print("\n=========================")
        print("# what is bundid".upper())
        print(f"\n{dropdown1text1.text}")
        print(f"\n{dropdown1text2.text}")
        print(f"\n{dropdown1text3.text}")

        #How do i use bundid dropdown
        dropdown2=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[1]/div[3]/button[1]")))
        dropdown2.click()
        dropdown2text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[normalize-space()='Your BundID has two important features:']")))
        dropdown2text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[contains(text(),'Proving your identity')]")))
        dropdown2text3=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[contains(text(),'Receiving official communications')]")))
        print("\n=========================")
        print("How do i use bundid".upper())
        print(f"\n{dropdown2text1.text}")
        print(f"\n{dropdown2text2.text}")
        print(f"\n{dropdown2text3.text}")

        # why should i create a bundid account dropdown
        dropdown3=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[1]/div[4]/button[1]")))
        dropdown3.click()
        dropdown3text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'You will need a BundID account to digitally prove ')]")))
        dropdown3text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'t have a BundID account, you can file individual o')]")))
        print("\n=========================")
        print("why should i create a bundid account".upper())
        print(f"\n{dropdown3text1.text}")
        print(f"\n{dropdown3text2.text}")

        # what are insurrance levels,means of identification and credentials dropdown
        dropdown4=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[1]/div[5]/button[1]")))
        dropdown4.click()
        dropdown4text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Each type of online request requires a certain lev')]")))
        dropdown4text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[normalize-space()='A means of identification']")))
        dropdown4text3=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[normalize-space()='is the way your personal data are established;']")))
        dropdown4text4=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[normalize-space()='has a certain level of assurance; and']")))
        dropdown4text6=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[normalize-space()='is a credential for accessing BundID']")))
        dropdown4text7=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'This is in line with the requirements of the EU Re')]")))
        dropdown4text8=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'There are three assurance levels, with specific me')]")))
        dropdown4text9=wait.until(EC.element_to_be_clickable((By.XPATH,"//b[normalize-space()='Basic registration']")))
        dropdown4text10=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'At this assurance level, you can use Username & Pa')]")))
        dropdown4text11=wait.until(EC.element_to_be_clickable((By.XPATH,"//b[normalize-space()='High']")))
        dropdown4text12=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'At this assurance level, you can use your eID card')]")))
        print("\n=========================")
        print("what are insurrance levels,means of identification and credentials\n".upper())
        print(f"\n{dropdown4text1.text}")
        print(f"\n{dropdown4text2.text}")
        print(f"\n{dropdown4text3.text}")
        print(f"\n{dropdown4text4.text}")
        print(f"\n{dropdown4text6.text}")
        print(f"\n{dropdown4text7.text}")
        print(f"\n{dropdown4text8.text}")
        print(f"\n{dropdown4text9.text}")
        print(f"\n{dropdown4text10.text}")
        print(f"\n{dropdown4text11.text}")
        print(f"\n{dropdown4text12.text}")


        # How do I file an Online request dropdown
        dropdown5=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[1]/div[6]/button[1]")))
        dropdown5.click()
        dropdown5text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Until recently, the only way to file a request was')]")))
        print("\n=========================")
        print("How do I file an Online request".upper())
        print(f"\n{dropdown5text1.text}")


        # Why is the option 'eID card' recommended dropdown
        dropdown6=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[1]/div[7]/button[1]")))
        dropdown6.click()
        dropdown6text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'An eID card (e.g. your national identity card) can')]")))
        dropdown6text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'When logged in with an eID card, you can open and ')]")))
        print("\n=========================")
        print("Why is the option 'eID card' recommended".upper())
        print(f"\n{dropdown6text1.text}")
        print(f"\n{dropdown6text2.text}")


        # How do I request an eID dropdown
        dropdown7=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[1]/div[8]/button[1]")))
        dropdown7.click()
        dropdown7text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Identity card with online ID function:')]")))
        dropdown7text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'t have to request this identity card.')]")))
        dropdown7text3=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'eID card for EU/EEA citizens: citizens of the Euro')]")))
        dropdown7text4=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Learn more about electronic identities')]")))
        print("\n=========================")
        print("How do I request an eID".upper())
        print(f"\n{dropdown7text1.text}")
        print(f"\n{dropdown7text2.text}")
        print(f"\n{dropdown7text3.text}")
        print(f"\n{dropdown7text4.text}")


        # Do I have to create a BundID account to file an online request dropdown
        dropdown8=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[1]/div[9]/button[1]")))
        dropdown8.click()
        dropdown8text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'No. You can also log in as a guest. In this case, ')]")))
        dropdown8text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Please note, however, that with a guest login you ')]")))
        print("\n=========================")
        print("Do I have to create a BundID account to file an online request".upper())
        print(f"\n{dropdown8text1.text}")
        print(f"\n{dropdown8text2.text}")


        # How do I create a bundid account dropdown
        dropdown9=wait.until(EC.element_to_be_clickable((By.XPATH,"//article[2]//div[2]//button[1]")))
        dropdown9.click()
        # dropdown9text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='0.8593113054678676']//p[1]")))
        dropdown9text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[normalize-space()='Username & Password']")))
        dropdown9text3=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[normalize-space()='eID card']")))
        dropdown9text4=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[normalize-space()='ELSTER certificate']")))
        dropdown9text5=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[normalize-space()='EU Identity']")))
        dropdown9text6=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Select an option and follow the steps to verify yo')]")))
        dropdown9text7=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Each of these options represents one credential.')]")))
        print("\n\n=========================")
        print("How do I create a bundid account".upper())
        # print(f"\n{dropdown9text1.text}")
        print(f"\n{dropdown9text2.text}")
        print(f"\n{dropdown9text3.text}")
        print(f"\n{dropdown9text4.text}")
        print(f"\n{dropdown9text5.text}")
        print(f"\n{dropdown9text6.text}")
        print(f"\n{dropdown9text7.text}")



        # How can I log in to bundid account dropdown
        dropdown10=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[2]/div[3]/button[1]")))
        dropdown10.click()
        dropdown10text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Once you have created a BundID account, you can lo')]")))
        dropdown10text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'If you added more credentials to your BundID accou')]")))
        print("\n\n=========================")
        print("How can I log in to bundid account".upper())
        print(f"\n{dropdown10text1.text}")
        print(f"\n{dropdown10text2.text}")


        # Why do I need AusweisApp dropdown
        dropdown11=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[2]/div[4]/button[1]")))
        dropdown11.click()
        dropdown11text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'You need AusweisApp to read data from your eID car')]")))
        dropdown11text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Note: AusweisApp does not work with your browser i')]")))
        dropdown11text3=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'If you see an error message while trying to log in')]")))
        dropdown11text4=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'In rare cases, errors may be caused by an NFC malf')]")))
        print("\n\n=========================")
        print("How can I log in to bundid account".upper())
        print(f"\n{dropdown11text1.text}")
        print(f"\n{dropdown11text2.text}")
        print(f"\n{dropdown11text3.text}")
        print(f"\n{dropdown11text4.text}")



        # Can I use my De-Mail address for bundid dropdown
        dropdown12=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[2]/div[5]/button[1]")))
        dropdown12.click()
        dropdown12text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'You cannot send or receive De-Mail messages with B')]")))
        dropdown12text2=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Note: De-Mail can be used through authorised servi')]")))
        print("\n\n=========================")
        print("Can I use my De-Mail address for bundid".upper())
        print(f"\n{dropdown12text1.text}")
        print(f"\n{dropdown12text2.text}")


        # Which data are stored and what happens to my data dropdown
        dropdown13=wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/article[1]/div[2]/article[2]/div[6]/button[1]")))
        dropdown13.click()
        dropdown13text1=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[contains(text(),'Please see our')]")))
        print("\n\n=========================")
        print("Can I use my De-Mail address for bundid".upper())
        print(f"\n{dropdown13text1.text}")
        print("\n\nComplete!".upper())

    except requests.ConnectionError:
        print("\n\nInternet disconnected.".upper())

    except TimeoutException:
        print("\n\nInternet is slow or page took too long to load".upper())
    finally:
        sys.exit()

BundIDAutoGetText()