from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
# Start Chrome WebDriver with options
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open the URL
driver.get("https://kefeta-dhis.amref.org/dhis-web-commons/security/login.action")

# Wait for the username field to be visible
username = wait.until(EC.visibility_of_element_located((By.ID, "j_username")))
username.send_keys("EdenY")

# Wait for the password field to be visible
password = wait.until(EC.visibility_of_element_located((By.ID, "j_password")))
password.send_keys("P@ssword1")

# Click on the Sign In button
signin = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
signin.click()

# Define a function to handle StaleElementReferenceException and retry the operation
def retry_click(element):
    try:
        element.click()
    except StaleElementReferenceException:
        retry_click(element)


menu= wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@data-test="headerbar-apps-icon"]')))
retry_click(menu)
# Click on the Tracker Capture link
tracker_capture = wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@href="../api/../dhis-web-tracker-capture/index.action"]')))
retry_click(tracker_capture)

#wait 5 seconds and click the dropdown button 
time.sleep(5)
toggle= driver.find_element(By.XPATH, '//span[@class="select2-arrow ui-select-toggle"]')
toggle.click()

#find youth tally and then click it to see the list
time.sleep(2)
youth_tally= wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@ng-bind-html="program.displayName | highlight: $select.search"]')))
retry_click(youth_tally)

time.sleep(5)
#click register button to go to register form
register= driver.find_element(By.LINK_TEXT,'Register')
register.click()


