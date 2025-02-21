from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException 
import csv, time


tables = []
chairs = []
sofas = []

error_list = []

driver = webdriver.Firefox()

# Passes through the cookies popup
driver.get("https://www.chilli.se/inredning")
driver.implicitly_wait(0.5)
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
tables = []
chairs = []
sofas = []
def scrape_products(x_current, x_target, position, xpath_template, target_url, product_list, amount_of_pages, xpath_first_page):

    driver.get(target_url)
    change_template = False

    for current_page in range(0, amount_of_pages):
        
        while x_current <= x_target: 

            #Updates xpath dynamically by formatting x_current each run to allow for use on other sites 
            try:

                if change_template == False:
                    try:
                        xpath = xpath_template.format(x_current=x_current, position=position) 
                        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                        print("Product " + str(x_current) + ", page " + str((current_page + 1)) + " located at " + xpath + "!")

                    except NoSuchElementException :
                        change_template = True
                        xpath = xpath_template.format(x_current=x_current, position=position - 1
                                                      )
                        print("Attempting to find the xpath at " + xpath + "...")
                        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

                        print("\033[93mDid not find the xpath, switched to xpath_template_alt\033[0m")
                        print(driver.current_url)
                else:
                    xpath = xpath_template.format(x_current=x_current, position=position - 1)
                    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                    print("Product " + str(x_current) + " located at " + xpath + "!")

                # Gets attributes from the selected product and then goes back a page
                name = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/h1").text
                image_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div/div[2]/div[1]/div/div/div[1]/img")
                src = image_element.get_attribute("src")

                # Checks to see if there is a product description for the current product
                try:
                    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/h3"))).click()     
                    try:
                        # Wait for the description text to appear after clicking
                        description = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/div/div/p[1]").text

                    except NoSuchElementException:
                        print("\033[93mThere was no product description!\033[93m")
                        description = "No description exists for this product!"

                except TimeoutException:
                    print("\033[93mThere was no product description!\033[93m")
                    description = "No description exists for this product!"

                # Attempts to locate the price div
                price_div = ["/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div[2]/span[2]", "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[1]/div/span[2]", "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div/span[2]"]
                y = 0
                for div in price_div:
                    y += 1
                    try:
                        price = driver.find_element(By.XPATH, div).text
                        print("\033[92mFound price " + price + "\033[0m")
                        break
                    except NoSuchElementException :
                        if y == 3:
                            print("\033[91mPrice not found on last attempt, skipping product!\033[0m")
                        else:
                            print("\033[93mPrice not found on attempt #" + str(y) + "! Trying again\033[0m")


                url = driver.current_url
                product = [name, description, price, src, url]
                product_list.append(product)
                driver.back()
                x_current += 1  

            except NoSuchElementException :
                print("\033[91mProduct " + str(x_current) + " could not be saved!\033[0m")
                error_list.append["Error with product " + str(x_current)]
                x_current += 1
                driver.back()
        # Sorts through the bottom divs to make sure it can find the next page
        if current_page == 0:
            driver.implicitly_wait(1)
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath_first_page))).click()                                                                              
            print("\033[93mSuccessfully switched to " + driver.current_url + "\033[0m")

            x_current = 1
        elif current_page == amount_of_pages:
            return product_list
        elif current_page > 0 and current_page != amount_of_pages:         
            y = 0                                                                                                                                       
            next_page = ["/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[7]", "/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[6]", "/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[4]"]
            for div in next_page:
                y += 1
                try:      
                    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, div))).click()            
                except:    
                    if y == 3:  
                        print(print("\033Current div does not work: " + div + "\033[0m"))                                                                                                                                                                                                                                                                                             
                    else:
                         print("\033[93mStandard xpath did not work, attempt a new div instead\033[0m")    
            print("\033[92mFound the next page button!\033[0m")
            print("\033[93mSuccessfully switched to " + driver.current_url + "\033[0m")
            x_current = 1
    return product_list


# Searches through nordicnest and targets all the tables on the first page
x_current = 1
x_target = 24
amount_of_pages = 3
position = 6
xpath_first_page = "/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[4]"
xpath_template = "/html/body/div[1]/div/main/div/div[2]/div[2]/ul/li[{x_current}]/div/a"          
target_url = "https://www.chilli.se/m%C3%B6bler/bord/matbord-k%C3%B6ksbord"

start_time = time.time()
tables = scrape_products(x_current, x_target, position, xpath_template, target_url, tables, amount_of_pages, xpath_first_page)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Table scrape took: {elapsed_time:.2f} seconds")

x_current = 1
x_target = 24
amount_of_pages = 3
position = 6
xpath_first_page = "/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[4]"
xpath_template = "/html/body/div[1]/div/main/div/div[2]/div[2]/ul/li[{x_current}]/div/a"          
target_url = "https://www.chilli.se/m%C3%B6bler/stolar/matstolar-k%C3%B6ksstolar"

start_time = time.time()
chairs = scrape_products(x_current, x_target, position, xpath_template, target_url, chairs, amount_of_pages, xpath_first_page)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Chairs scrape took: {elapsed_time:.2f} seconds")

x_current = 1
x_target = 24
amount_of_pages = 3
position = 6
xpath_first_page = "/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[4]"
xpath_template = "/html/body/div[1]/div/main/div/div[2]/div[2]/ul/li[{x_current}]/div/a"          
target_url = "https://www.chilli.se/m%C3%B6bler/soffor"

start_time = time.time()
sofas = scrape_products(x_current, x_target, position, xpath_template, target_url, sofas, amount_of_pages, xpath_first_page)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Sofas scrape took: {elapsed_time:.2f} seconds")

# Writes the products into extended tables
if tables != None:
    with open('chilli_tables.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Description", "Price", "Image URL", "Product URL"])  # Header row
        for table in tables:
            writer.writerow(table)
        print("\033[92mData saved to chilli_tables.csv!\033[0m")
else:
    print("\033[91mThere was an error with saving chilli_tables file!\033[0m")

if chairs != None:
    with open('chilli_chairs.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Description", "Price", "Image URL", "Product URL"])  # Header row
        for chair in chairs:
            writer.writerow(chair)
        print("\033[92mData saved to chilli_chairs.csv!\033[0m")
else:
    print("\033[91mThere was an error with saving chilli_chairs file!\033[0m")

if sofas != None:
    with open('chilli_sofas.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Description", "Price", "Image URL", "Product URL"])  # Header row
        for sofa in sofas:
            writer.writerow(sofa)
        print("\033[92mData saved to chilli_sofas.csv!\033[0m")
else:
    print("\033[91mThere was an error with saving chilli_sofas file!\033[0m")

driver.quit()



