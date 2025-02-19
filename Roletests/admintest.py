from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def admin_test():
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

    email_box.send_keys("admin@mail.se")
    time.sleep(0.5)
    password_box = driver.find_element(By.NAME, "password")

    password_box.send_keys("admin123")
    time.sleep(0.5)
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    login_button.click()

    current_url = driver.current_url
    print("\033[93m" + current_url + "\033[93m")

    driver.get("http://127.0.0.1/marketplace_1/public_html/users")

    result = driver.find_element(By.XPATH, "//p[text()='Welcome, Admin! You have full access.']").text

    if result == "Welcome, Admin! You have full access.":

        selectUser = driver.find_element(By.XPATH, "//tr[.//td[contains(text(), '8ea1383d-baf9-4cf3-8f7c-0da805ae5759')]]")

        edit_button = selectUser.find_element(By.CSS_SELECTOR, ".btn.btn-sm.btn-warning")
        edit_button.click()
        current_role = driver.find_element(By.XPATH, "//form[.//div[.//h4[contains(text(), 'Current Roles:')]]]/div//h2").text
        

        if current_role == "admin":
            select_element = driver.find_element(By.ID, "newRole")
            select = Select(select_element)

            select.select_by_value("client")

            save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save Changes')]")
            save_button.click()

            print("\033[92mTest Succes, changed role from admin to client!\033[92m")
        elif current_role == "client":

            select_element = driver.find_element(By.ID, "newRole")
            select = Select(select_element)

            select.select_by_value("admin")

            save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save Changes')]")
            save_button.click()
            print("\033[92mTest Succes, changed role from client to admin!\033[92m")
    else:
        print("\033[91mTest failed, admin can't access users page!\033[91m")

    

    driver.quit()