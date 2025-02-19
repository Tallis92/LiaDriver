from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://127.0.0.1/marketplace_1/public_html/pizzashop/")
current_url = driver.current_url

print(current_url)
driver.implicitly_wait(1)

title = driver.title

print(title)
print("==================")
labels = driver.find_elements(By.CLASS_NAME, value="card-title")

for label in labels:
    print(label.text)

print("================")
shrimpPizza = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Shrimp Pizza')]]")
shrimpLabel = shrimpPizza.find_element(By.TAG_NAME, "h5").text

print("There it is! The infamous " + shrimpLabel)
print("============")

numbers = [1, 2]

for number in numbers:

    driver.implicitly_wait(1)

    shrimpPizza = driver.find_element(By.XPATH, "//div[@class='card-body' and .//h5[contains(text(), 'Shrimp Pizza')]]")
    
    add_button = shrimpPizza.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

    add_button.click()


    current_url2 = driver.current_url

    print(current_url2)

    baseQuantity = driver.find_element(By.XPATH, "//input[@name='quantity']")
    quantityValue = baseQuantity.get_attribute("value")

    print("Quantity value = " + quantityValue)

    return_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue Shopping')]")
    if number == 1:
        return_button.click()
        current_url = driver.current_url
        print(current_url)

print("=============")
print("Time to check it out!")
print("=============")

checkout_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary[href*='checkout']")
checkout_button.click()

current_url = driver.current_url
print(current_url)

currencyAmount = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@id='ProductSummary-totalAmount']//span[@class='CurrencyAmount']"))
)
#currencyAmount = driver.find_element(By.CSS_SELECTOR, ".ProductSummary-totalAmount .CurrencyAmount")

numeric_value = float(currencyAmount.text.replace("US$", "").replace(",", ".").strip())

print(numeric_value)
if numeric_value == 190:
    print("\033[92mTotal sum: " + str(numeric_value) + "\033[92m")
    print("\033[92mToday was a total success!\033[[0m")
else:
    print("\033[91mTotal sum is wrong, expected 195 vs actual " + str(numeric_value) + "\033[91m")
    print("\033[91mToday was a total failure\033[[0m")