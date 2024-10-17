from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the LinkedIn page
driver.get("https://www.linkedin.com")

# Log in to LinkedIn here if necessary

# Wait for the message button to be clickable
message_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Message']"))
)

# Click the message button
message_button.click()