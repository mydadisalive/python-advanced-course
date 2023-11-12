from selenium import webdriver

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.google.com")

# Close the browser
driver.quit()
