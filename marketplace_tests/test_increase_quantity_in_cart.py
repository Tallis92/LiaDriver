from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://127.0.0.1/marketplace_1/public_html/shop/")

kakel_element = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Kakel')]]")
add_button = kakel_element.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
add_button.click()

quantity_element = driver.find_element(By.NAME, "quantity")
quantity_element.clear()
quantity_element.send_keys("5")

quantity_element = driver.find_element(By.NAME, "quantity")
quantity = quantity_element.get_attribute("value")

update_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-sm.btn-secondary")
update_button.click()

quantity_element = driver.find_element(By.XPATH, "//strong[contains(text(), '$')]")
numeric_value = float(quantity_element.text.replace("$", "").replace(",", ".").strip())

if numeric_value == 500:
    print("\033[92mPassed: test_increase_quantity_in_cart.py\033[0m")
else:
    print("\033[91mFailed: test_increase_quantity_in_cart.py\033[0m")

driver.quit()