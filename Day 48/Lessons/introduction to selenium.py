# Link to selenium docs: https://selenium-python.readthedocs.io/

from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# Finding data through class name
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar}.{price_cents}")

# Finding data through name
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

# Finding data through id
button = driver.find_element(By.ID, value="submit")
print(button.size)

# Finding data through CSS selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# The line above taps into the div element and finds any anchor tag
print(documentation_link.text)

# IF all else fails use x path : https://www.w3schools.com/xml/xpath_intro.asp 

# # Closes a single tab.
# driver.close()
# # Quit closes the entire browser.
# driver.quit()


