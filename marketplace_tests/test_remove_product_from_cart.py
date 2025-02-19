from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# user adds item to cart
driver.get("http://127.0.0.1/marketplace_1/public_html/shop/")
kakel_element = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Kakel')]]")

add_kakel = kakel_element.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
add_kakel.click()

# user removes item from cart
remove_kakel = driver.find_element(By.CSS_SELECTOR, ".btn.btn-sm.btn-danger")
remove_kakel.click()

# checks for the "empty" <p>-tag

is_empty = driver.find_element(By.XPATH, "//p[contains(text(), 'Your cart is empty.')]").text

if is_empty == "Your cart is empty.":
    print("\033[92mPassed: test_remove_product_from_cart\033[0m")
else:
    print("\033[91mFailed: test_remove_product_from_cart\033[0m")

driver.quit()