from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# user adds item to cart
driver.get("http://127.0.0.1/marketplace_1/public_html/shop/")

numbers = [1, 2]

for number in numbers:
    kakel = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Kakel')]]")
    add_button = kakel.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    add_button.click()
    if number == 1:
        return_anchor = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue Shopping')]")
        return_anchor.click()

quantity_element = driver.find_element(By.NAME, "quantity")
quantity = quantity_element.get_attribute("value")

if int(quantity) == 2:

    total = driver.find_element(By.XPATH, "//strong[contains(text(), '$')]")
    numeric_value = float(total.text.replace("$", "").replace(",", ".").strip())

    if numeric_value == 200:
        print("\033[92mPassed: test_add_the_same_product_to_cart_twice.py\033[0m")
    else:
        print("\033[91mFailed: test_add_the_same_product_to_cart_twice.py\033[0m")
        print("\033[91mTotal price did not align with the expected value of 200.\033[0m]")
        print("\033[91mActual value: {quantity}\033[0m")
else:
    print("\033[91mFailed: test_add_the_same_product_to_cart_twice.py\033[0m")
    print("\033[91mProduct quantity did not align with the expected value of 2.\033[0m]")
    print("\033[91mActual value: {quantity}\033[0m")

driver.quit()