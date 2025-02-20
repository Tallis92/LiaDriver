from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv
import time

tables = []
chairs = []
sofas = []

driver = webdriver.Edge()

# Passes through the cookies popup
driver.get("https://www.chilli.se/inredning")
driver.implicitly_wait(5)
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
tables = []
chairs = []
sofas = []
def scrape_products(x_current, x_target, position, xpath_template, target_url, product_list, amount_of_pages, xpath_first_page):

    driver.get(target_url)
    change_template = False
    for current_page in range(0, amount_of_pages):
        
        # Makes sure the application doesn't iterate more times than it needs to
        # if current_page == amount_of_pages:
        #     print("\033[93mSuccessfully broke the loop!\033[0m")
        #     break

        while x_current <= x_target:
            driver.implicitly_wait(5)  

            #Updates xpath dynamically by formatting x_current each run to allow for use on other sites
            
            try:

                if change_template == False:
                    try:
                        xpath = xpath_template.format(x_current=x_current, position=position) 
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                        print("Product " + str(x_current) + " located at " + xpath + "!")
                    except:
                        change_template = True
                        xpath = xpath_template.format(x_current=x_current, position=position - 1)
                        print("Attempting to find the xpath at " + xpath + "...")
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                        print("\033[93mDid not find the xpath, switched to xpath_template_alt\033[0m")
                        print(driver.current_url)
                else:
                    xpath = xpath_template.format(x_current=x_current, position=position - 1)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                    print("Product " + str(x_current) + " located at " + xpath + "!")

                driver.implicitly_wait(5)

                # Gets attributes from the selected product and then goes back a page
                name = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/h1").text
                image_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div/div[2]/div[1]/div/div/div[1]/img")
                src = image_element.get_attribute("src")
                try:
                    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/h3"))).click()
                    driver.implicitly_wait(1)  
                    description = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/div/div/p[1]").text
                except:
                    print("There was no product description!")
                    description = "No description exists for this product..."            
                price = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[1]/div").text
                url = driver.current_url
                product = [name, description, price, src, url]
                product_list.append(product)
                driver.back()
                x_current += 1  
            except:
                print("\033[91mProduct " + str(x_current) + " could not be located!\033[0m")
                x_current += 1
                driver.back()
        # Sorts through the bottom divs to make sure it can find the next page
        if current_page == 0:
            driver.implicitly_wait(1)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath_first_page))).click()
                                                                                    
            print("\033[93mSuccessfully switched to " + driver.current_url + "\033[0m")
            x_current = 1
        elif current_page > 0 and current_page != amount_of_pages:
            driver.implicitly_wait(5)
            try:
                selectPage = 3
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[{selectPage}]"))).click()
            except:                                                                  
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[{selectPage + 2}]"))).click()
                print("\033[93m Standard xpath did not work, attempt to find /html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[5] instead\033[0m")                                     
            print("\033[93mSuccessfully switched to " + driver.current_url + "\033[0m")
            x_current = 1
        
    return product_list


# Searches through nordicnest and targets all the tables on the first page
x_current = 1
x_target = 24
amount_of_pages = 3
position = 6
xpath_first_page = "/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[3]"
xpath_template = "/html/body/div[1]/div/main/div/div[2]/div[2]/ul/li[{x_current}]/div/a"          
target_url = "https://www.chilli.se/m%C3%B6bler/bord/matbord-k%C3%B6ksbord"

tables = scrape_products(x_current, x_target, position, xpath_template, target_url, tables, amount_of_pages, xpath_first_page)