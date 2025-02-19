from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def client_test():
    # options = Options()

    # options = webdriver.Chrome()
    # options.add_argument("--disable-search-engine-choice-screen")
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Firefox()

    driver.get("http://127.0.0.1/marketplace_1/public_html/")
    current_url = driver.current_url
    print("\033[93m" + current_url + "\033[93m")

    login_anchor = driver.find_element(By.XPATH, "//a[@class='nav-link' and .//span[contains(text(), 'Login')]]")

    login_anchor.click()

    current_url = driver.current_url
    print("\033[93m" + current_url + "\033[93m")


    email_box = driver.find_element(By.NAME, "email")

    email_box.send_keys("client@mail.com")
    time.sleep(0.5)
    password_box = driver.find_element(By.NAME, "password")

    password_box.send_keys("abc123")
    time.sleep(0.5)
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    login_button.click()

    current_url = driver.current_url
    print("\033[93m" + current_url + "\033[93m")

    driver.get("http://127.0.0.1/marketplace_1/public_html/users")

    result = driver.find_element(By.XPATH, "//p[text()='You do not have admin privileges.']").text

    if result == "You do not have admin privileges.":
        print("\033[92mTest succes, client was denied access to user page!\033[0m")
    else:
        print("\033[91mTest failed, client could access user page!\033[0m")

    driver.quit()

