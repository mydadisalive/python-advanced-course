from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://sol2014.sela.co.il/SOL/SisyLoginSecure.aspx?ReturnUrl=%2fSOL%2fLecturers%2fLectureTrainingSchedule.aspx")

# Find the username and password fields and fill them out

username_field = driver.find_element(By.ID, "logAdmin_UserName")
password_field = driver.find_element(By.ID, "logAdmin_Password")

time.sleep(5)

username_field.send_keys("user@gmail.com")
password_field.send_keys("blabla")

time.sleep(5)

# Submit the form
login_button = driver.find_element(By.ID, "logAdmin_LoginButton")
login_button.click()

time.sleep(5)

driver.quit()
