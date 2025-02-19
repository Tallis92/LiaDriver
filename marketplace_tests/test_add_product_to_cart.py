from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# user adds item to cart
driver.get("http://127.0.0.1/marketplace_1/public_html/shop/")

kakel_element = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Kakel')]]")
add_kakel = kakel_element.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

add_kakel.click()

# Checks carts total sum
total = driver.find_element(By.XPATH, "//strong[contains(text(), '$')]")
numeric_value = float(total.text.replace("$", "").replace(",", ".").strip())

if numeric_value == 100:
    print("\033[92mPassed: test_add_product_to_cart.py\033[0m")
else:
    print("\033[91mFailed: test_add_product_to_cart.py\033[0m")

driver.quit()