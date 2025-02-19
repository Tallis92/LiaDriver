from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

## TODO: Add if statements inside the scrape_product method to make sure that it won't crash if it doesn't find the correct divs
## TODO: Add filewriting to a specific path
tables = []
chairs = []
sofas = []

driver = webdriver.Firefox()

# Passes through the cookies popup
driver.get("https://www.nordicnest.se/")
driver.implicitly_wait(5)
driver.find_element(By.ID, "acceptAllBtn").click()

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
            
            

            if change_template == False:
                try:
                    xpath = xpath_template.format(x_current=x_current, position=position) 
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                    print("Product " + str(x_current) + " located at " + xpath + "!")
                except:
                    change_template = True
                    xpath = xpath_template.format(x_current=x_current, position=position - 1)

                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                    print("\033[93mDid not find the xpath, switched to xpath_template_alt\033[0m")
            else:
                xpath = xpath_template.format(x_current=x_current, position=position - 1)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                print("Product " + str(x_current) + " located at " + xpath + "!")

            driver.implicitly_wait(5)

            # Gets attributes from the selected product and then goes back a page
            name = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[1]/h1").text
            image_element = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/img")
            src = image_element.get_attribute("src")
            description = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div[1]/div/div").text
            price = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[2]/div[3]/div/div[1]/span").text
            url = driver.current_url
            product = [name, description, price, src, url]
            product_list.append(product)
            driver.back()
            x_current += 1

        # Sorts through the bottom divs to make sure it can find the next page
        if current_page == 0:
            driver.implicitly_wait(5)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath_first_page))).click()
                                                                                    
            print("\033[93mSuccessfully switched to " + driver.current_url + "\033[0m")
            x_current = 1
        elif current_page > 0 and current_page != amount_of_pages:
            driver.implicitly_wait(5)
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[4]/div[6]/div[2]/div[2]/div/a[6]"))).click()  
            except:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[4]/div[5]/div[2]/div[2]/div/a[6]"))).click()
                print("\033[93m Standard xpath did not work, attempt to find /html/body/div[3]/div[4]/div[5]/div[2]/div[2]/div/a[6] instead\033[0m")                                     
            print("\033[93mSuccessfully switched to " + driver.current_url + "\033[0m")
            x_current = 1
        
    return product_list


# Searches through nordicnest and targets all the tables on the first page
x_current = 1
x_target = 36
amount_of_pages = 3
position = 6
xpath_first_page = "/html/body/div[3]/div[4]/div[6]/div[2]/div[2]/div/a[4]"
xpath_template = "/html/body/div[3]/div[4]/div[{position}]/div[1]/ul/li[{x_current}]/div/a"              
target_url = "https://www.nordicnest.se/mobler/bord/"

tables = scrape_products(x_current, x_target, position, xpath_template, target_url, tables, amount_of_pages, xpath_first_page)

# Searches through nordicnest and targets all the chairs on the first page

x_current = 1
x_target = 36
amount_of_pages = 3
position = 6
target_url = "https://www.nordicnest.se/mobler/stolar--pallar/stolar/"

chairs = scrape_products(x_current, x_target, position, xpath_template, target_url, chairs, amount_of_pages, xpath_first_page)


# Searches through nordicnest and targets all the sofas on the first page

x_current = 1
x_target = 36
amount_of_pages = 3 
position = 7
xpath_first_page =  "/html/body/div[3]/div[4]/div[7]/div[2]/div[2]/div/a[4]"
xpath_template = "/html/body/div[3]/div[4]/div[{position}]/div[1]/ul/li[{x_current}]/div/a"
target_url = "https://www.nordicnest.se/mobler/soffor--fatoljer/soffor/"

sofas = scrape_products(x_current, x_target, position, xpath_template, target_url, sofas, amount_of_pages, xpath_first_page)


# Writes the products into extended tables
if tables != None:
    with open('nordicnest_tables.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Description", "Price", "Image URL", "Product URL"])  # Header row
        for table in tables:
            writer.writerow(table)
        print("\033[92mData saved to nordicnest_tables.csv!\033[0m")
else:
    print("\033[91mThere was an error with saving nordicnest_tables file!\033[0m")

if chairs != None:
    with open('nordicnest_chairs.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Description", "Price", "Image URL", "Product URL"])  # Header row
        for chair in chairs:
            writer.writerow(chair)
        print("\033[92mData saved to nordicnest_chairs.csv!\033[0m")
else:
    print("\033[91mThere was an error with saving nordicnest_chairs file!\033[0m")

if sofas != None:
    with open('nordicnest_sofas.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Description", "Price", "Image URL", "Product URL"])  # Header row
        for sofa in sofas:
            writer.writerow(sofa)
        print("\033[92mData saved to nordicnest_sofas.csv!\033[0m")
else:
    print("\033[91mThere was an error with saving nordicnest_sofas file!\033[0m")

driver.quit()
    


