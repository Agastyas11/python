import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from passwords import *

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4069340956&f_AL=true&geoId=101265034&keywords=fast%20food%20crew%20member&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&sortBy=R")

# Sign in
time.sleep(2)
sign_in = driver.find_element(By.CSS_SELECTOR, "#base-contextual-sign-in-modal > div > section > div > div > div > div.sign-in-modal > button")
sign_in.click()

email_or_phone = driver.find_element(By.CSS_SELECTOR, value="#base-sign-in-modal_session_key")
your_password = driver.find_element(By.CSS_SELECTOR, value="#base-sign-in-modal_session_password")

email_or_phone.send_keys(email, Keys.ENTER)
your_password.send_keys(password, Keys.ENTER)

# Easy Apply
time.sleep(5)
easy_apply = driver.find_element(By.XPATH, '//*[@id="ember54"]')
easy_apply.click()

# Add phone number
time.sleep(3)
phone_number = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4069340956-1607701605986365007-phoneNumber-nationalNumber"]')
phone_number.send_keys(phonenumber, Keys.ENTER)

# Click next
(driver.find_element(By.XPATH, '//*[@id="ember387"]')).click()

# Home address
time.sleep(2)
home_address = driver.find_element(By.XPATH, value='//*[@id="single-typeahead-entity-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4069340956-6916279094326431486-city-HOME-CITY"]')
home_address.send_keys(address, Keys.ENTER)

# Click next
(driver.find_element(By.CSS_SELECTOR, '//*[@id="ember387"]')).click()





