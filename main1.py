from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

# Start Chrome WebDriver with options

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get("https://kefeta-dhis.amref.org/dhis-web-commons/security/login.action")
time.sleep(5)

# Enter text in the First name field
username = driver.find_element(By.ID, "j_username")
username.send_keys("EdenY")

# Enter text in the Last name field
password = driver.find_element(By.ID, "j_password")
password.send_keys("P@ssword1")


signin = driver.find_element(By.ID, "submit")
signin.click()

time.sleep(5)