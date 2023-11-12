from selenium import webdriver
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.google.com")

time.sleep(5)

# Close the browser
driver.quit()
