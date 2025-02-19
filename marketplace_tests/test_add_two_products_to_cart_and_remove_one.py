from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# user adds item to cart
driver.get("http://127.0.0.1/marketplace_1/public_html/shop/")

kakel_element = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Kakel')]]")
add_button = kakel_element.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
add_button.click()

return_anchor = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue Shopping')]")
return_anchor.click()

tapet_element = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Tapet')]]")
add_button = tapet_element.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
add_button.click()

remove_button = driver.find_element(By.XPATH, "//table//tr[1]//a[@class='btn btn-sm btn-danger']")
remove_button.click()

quantity_element = driver.find_element(By.XPATH, "//strong[contains(text(), '$')]")
quantity = float(quantity_element.text.replace("$", "").replace(",", ".").strip())

if quantity == 50:
    print("\033[92mPassed: test_add_two_products_to_card_and_remove_one.py\033[0m")
else:
    print("\033[91mFailed: test_add_two_products_to_card_and_remove_one.py\033[0m")
