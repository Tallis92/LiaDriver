from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()


driver.get("http://127.0.0.1/marketplace_1/public_html/")
current_url = driver.current_url
print("\033[93m" + current_url + "\033[0m")

login_anchor = driver.find_element(By.XPATH, "//a[@class='nav-link' and .//span[contains(text(), 'Login')]]")

login_anchor.click()

# User logs in
email_box = driver.find_element(By.NAME, "email")
email_box.send_keys("client@mail.com")

password_box = driver.find_element(By.NAME, "password")
password_box.send_keys("abc123")

login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
login_button.click()

# user adds item to cart
driver.get("http://127.0.0.1/marketplace_1/public_html/shop/")
kakel_element = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Kakel')]]")

add_kakel = kakel_element.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

add_kakel.click()

# user checksout cart
checkout_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary[href*='checkout']")
checkout_button.click()

current_url = driver.current_url
print("\033[93m" + current_url + "\033[0m")

driver.implicitly_wait(5)

email_box = driver.find_element(By.NAME, "email")
email_box.send_keys("client@mail.com")

cardnumber_box = driver.find_element(By.NAME, "cardNumber")
cardnumber_box.send_keys("4242 4242 4242 4242")

cardexpiry_box = driver.find_element(By.NAME, "cardExpiry")
cardexpiry_box.send_keys("0926")

cardcvc_box = driver.find_element(By.NAME, "cardCvc")
cardcvc_box.send_keys("345")

billingname_box = driver.find_element(By.NAME, "billingName")
billingname_box.send_keys("Client Clientsson")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".SubmitButton--complete"))
)

WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".SubmitButton-SpinnerIcon"))
)


submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".SubmitButton--complete"))
)

submit_button.click()

current_url = driver.current_url
print("\033[93m" + current_url + "\033[0m")

result = driver.find_element(By.XPATH, "//h1[contains(text(), 'Thank you for your purchase!')]").text

print(result)
if result == "Thank you for your purchase!":
    print("\033[92mSuccess!\033[92m")

else:
    print("\033[91mFailure\033[91m")



driver.quit()