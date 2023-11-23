from selenium import webdriver

# 1. Open a browser and go to any website
url = "https://www.n12.co.il/"
driver = webdriver.Chrome()
driver.get(url)

# Set the zoom level to 67% using JavaScript
zoom_script = "document.body.style.zoom='67%'"
driver.execute_script(zoom_script)

# 2. Take a screenshot of the current page and save it to a file
driver.save_screenshot("screenshot.png")
print("Screenshot captured and saved.")

# 3. Retrieve the page source and save it to a text file
page_source = driver.page_source
with open("page_source.txt", "w", encoding="utf-8") as file:
    file.write(page_source)
print("Page source retrieved and saved.")

# 4. Close the browser
driver.quit()
