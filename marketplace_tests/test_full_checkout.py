from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random


driver = webdriver.Firefox()

driver.get("http://127.0.0.1/marketplace_1/public_html/")
current_url = driver.current_url
print("\033[93m" + current_url + "\033[0m")

login_anchor = driver.find_element(By.XPATH, "//a[@class='nav-link' and .//span[contains(text(), 'Login')]]")

login_anchor.click()

def slow_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.1))

# time.sleep(random.uniform(1, 2)) 

# User logs in
email_box = driver.find_element(By.NAME, "email")
slow_typing(email_box, "client@mail.com")

password_box = driver.find_element(By.NAME, "password")
slow_typing(password_box, "abc123")
password_box.send_keys(Keys.RETURN)
print("\033[92mUser logged in!\033[0m")
driver.get("http://127.0.0.1/marketplace_1/public_html/shop")

iPhone_element = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'iPhone')]]")
add_btn = iPhone_element.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
add_btn.click()

return_anchor = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue Shopping')]")
return_anchor.click()

kakel_element = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Kakel')]]")
add_btn = kakel_element.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
add_btn.click()

return_anchor = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue Shopping')]")
return_anchor.click()

tapet_element = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Tapet')]]")
add_btn = tapet_element.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
add_btn.click()

remove_btn = driver.find_element(By.XPATH, "//table//tr[1]//a[@class='btn btn-sm btn-danger']")
remove_btn.click()

kakel_quantity = driver.find_element(By.XPATH, "//table//tr[1]//input[@name='quantity']")
kakel_quantity.clear()
kakel_quantity.send_keys("10")

update_btn = driver.find_element(By.XPATH, "//table//tr[1]//button[@class='btn btn-sm btn-secondary mt-1']")
update_btn.click()

tapet_quantity = driver.find_element(By.XPATH, "//table//tr[2]//input[@name='quantity']")
tapet_quantity.clear()
tapet_quantity.send_keys("5")


update_btn = driver.find_element(By.XPATH, "//table//tr[2]//button[@class='btn btn-sm btn-secondary mt-1']")
update_btn.click()

total_element = driver.find_element(By.XPATH, "//strong[contains(text(), '$')]")
total_amount = float(total_element.text.replace("$", "").replace(",", "").strip())

if total_amount == float(1250):
    print("\033[92mTotal sum test passed!\033[0m")
else:
    print("\033[91mTotal sum test failed!\033[0m")
    driver.quit()

checkout_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'Checkout')]")
checkout_btn.click()

driver.implicitly_wait(5)
email_box = driver.find_element(By.NAME, "email")
slow_typing(email_box, "client@mail.com")

cardnumber_box = driver.find_element(By.NAME, "cardNumber")
slow_typing(cardnumber_box, "4242 4242 4242 4242")

cardexpiry_box = driver.find_element(By.NAME, "cardExpiry")
slow_typing(cardexpiry_box, "0926")

cardcvc_box = driver.find_element(By.NAME, "cardCvc")
slow_typing(cardcvc_box, "345")

billingname_box = driver.find_element(By.NAME, "billingName")
slow_typing(billingname_box, "Client Clientsson")
billingname_box.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

success_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thank you for your purchase!')]"))
)

if success_element.text == "Thank you for your purchase!":
      print("\033[92mCheckout test passed!\033[0m")
else:
    print("\033[91mCheckout test failed!\033[0m")
    driver.quit()

return_anchor = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue Shopping')]")
return_anchor.click()

logout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link' and span[contains(text(), 'Logout')]]"))
)

logout_btn.click()

print("\033[92mUser logged out passed!\033[0m")
driver.quit()

