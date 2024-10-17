from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

s = Service('C:\\Users\\MESSIE\\Documents\\Brightchamps\\Automation\\chromedriver-win64\\chromedriver-win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
wait=WebDriverWait(driver,100)

driver.get("https://www.amazon.com/stores/page/A8C9DDD6-D199-47CB-B055-211E15C1927B/?_encoding=UTF8&channel=pnsp&pd_rd_w=ULRM0&content-id=amzn1.sym.e7a46b19-edd1-45a9-83f0-c144ecbec927&pf_rd_p=e7a46b19-edd1-45a9-83f0-c144ecbec927&pf_rd_r=97RZFBCGHF386JRQSVDN&pd_rd_wg=QFM8b&pd_rd_r=53e93ff6-9b71-4f1a-ae19-7fe8e0d645d7&ref_=pd_hp_d_hero_unk")
driver.maximize_window()
searchbar=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='twotabsearchtextbox']")))
searchbar.send_keys("Samsung Galaxy",Keys.ENTER)
itemselect=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Galaxy A15 5G A Series Cell Phone, 128GB Unlocked Android Smartphone, AMOLED Display, Expandable Storage, Knox Security, Super Fast Charging, US Version, 2024, Blue Black']")))
itemselect.click()
producttitle=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@id='productTitle']")))
productprice=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='apex_desktop_newAccordionRow']//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']//span[@aria-hidden='true']")))
producturl=driver.current_url
os.system("cls")
print("===============================")
print(f"Product title : {producttitle.text}")
print(f"Product Price : {productprice.text}")
print(f"Product URL : {producturl}")