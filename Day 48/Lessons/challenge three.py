from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email_address = driver.find_element(By.NAME, value="email")

first_name.send_keys("Cristiano", Keys.ENTER)
last_name.send_keys("Ronaldo", Keys.ENTER)
email_address.send_keys("c.ronaldo@madrid.com", Keys.ENTER)
