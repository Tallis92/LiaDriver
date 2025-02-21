from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException 
from selenium.webdriver.firefox.options import Options
import csv, time


tables = []
chairs = []
sofas = []
error_list = []
final_times = []

def set_driver(target_url):

    if target_url == None or target_url == "":
        return webdriver.Firefox()
    
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options = options)
    driver.get(target_url)
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
    element.click()

    print("This works 1")
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "onetrust-pc-dark-filter"))
    )
    print("This works 2")
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "onetrust-pc-dark-filter ot-fade-in"))
    )
    print("This works 3")
    WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.XPATH, "//div[@class='onetrust-pc-dark-filter']"))
    )
    print("This works 4")

    # Double check and force remove overlay with JavaScript
    overlay = driver.execute_script("return document.querySelector('.onetrust-pc-dark-filter');")
    if overlay:
        print("Overlay still exists! Removing it now.")
        driver.execute_script("arguments[0].remove();", overlay)
    
    print("This also works 4")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul/li[1]/div/a")))
    return driver



def scrape_products(x_current, x_target, position, xpath_template, target_url, product_list, amount_of_pages, xpath_first_page):

    
    first_run = True
    for current_page in range(0, amount_of_pages):
        
        page_time_start = time.time()
        if first_run == True:
            print("first run")
            driver = set_driver(target_url)
            
        else:
            print("Consecutive run")
            driver = set_driver(next_page_url)
        print("This worked 5")  
        
        change_template = False
        while x_current <= x_target: 
            
            
            scrape_product_start = time.time()
            #Updates xpath dynamically by formatting x_current each run to allow for use on other sites 
            try:
                
                if change_template == False:
                    try:
                        print("Now trying to push the button")
                        xpath = xpath_template.format(x_current=x_current, position=position) 
                        print("Determined xpath for buttonclick")
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
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
                    print("Now trying to push the button")
                    xpath = xpath_template.format(x_current=x_current, position=position - 1)
                    print("Determined xpath for buttonclick")
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                    print("Product " + str(x_current) + " located at " + xpath + "!")

                # Gets attributes from the selected product and then goes back a page
                print("Trying to find name!")
                name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/h1"))).text
                                                     
                print("Name found")
                image_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div/div[2]/div[1]/div/div/div[1]/img")
                print("Image found")
                src = image_element.get_attribute("src")
                print("Image src")

                # Checks to see if there is a product description for the current product
                try:
                    print("Trying to find product description")
                    element = driver.find_elements(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/h3")
                    if element:
                        element[0].click()
                        print("Product description found")
                    #WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/h3"))).click()     
                    try:
                        # Wait for the description text to appear after clicking
                        print("Trying to find description content")
                        element = driver.find_elements(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/div/div/p[1]")
                        if element:
                            description = element[0].text
                        else:
                            description = "No description exists for this product!"
                    except NoSuchElementException:
                        print("\033[93mThere was no product description!\033[93m")
                        description = "No description exists for this product!"
                    print("Found product content")
                except TimeoutException:
                    print("\033[93mThere was no product description!\033[93m")
                    description = "No description exists for this product!"

                # Attempts to locate the price div
                price_div = ["/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div[2]/span[2]", "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[1]/div/span[2]", "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div/span[2]"]
                y = 0
                for div in price_div:
                    y += 1
                    element = driver.find_elements(By.XPATH, div)
                    if element:
                        price = element[0].text
                        print("\033[92mFound price " + price + "\033[0m")
                        break
                    else:
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
                time.sleep(1000)
                x_current += 1
                driver.back()

            scrape_product_end = time.time()
            elapsed_time_product = scrape_product_end - scrape_product_start
            print(f"===== Scrape Product took: {elapsed_time_product:.2f} seconds =====")
        # Sorts through the bottom divs to make sure it can find the next page
        if current_page == 0:
            element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath_first_page))) 
            next_page_url = element.get_attribute("href")
            first_run = False                                                                         
            print("\033[93mSuccessfully switched to " + driver.current_url + "\033[0m")
            driver.quit() 
            x_current = 1

        elif current_page > 0 and current_page != amount_of_pages:         
            y = 0                                                                                                                                       
            next_page = ["/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[7]", "/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[6]", "/html/body/div[1]/div/main/div/div[2]/div[3]/div[2]/div/a[4]"]
            for div in next_page:
                y += 1 
                try:     
                    elements = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, div)))
                    next_page_url = elements[0].get_attribute("href")  
                    driver.quit()

                except:    
                    if y == 3:  
                        print(print("\033Current div does not work: " + div + "\033[0m"))                                                                                                                                                                                                                                                                                             
                    else:
                         print("\033[93mStandard xpath did not work, attempt a new div instead\033[0m") 

            print("\033[92mFound the next page button!\033[0m")
            print("\033[93mSuccessfully switched to " + driver.current_url + "\033[0m")
            driver.quit()
            page_time_end = time.time()
            elapsed_page_time = page_time_end - page_time_start
            print(f"===== Scrape Product took: {elapsed_page_time:.2f} seconds =====")
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
print(f"Entire Table Scrape took: {elapsed_time:.2f} seconds")
final_times.append(f"Entire Table Scrape took: {elapsed_time:.2f} seconds")

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
print(f"Entire Chairs scrape took: {elapsed_time:.2f} seconds")
final_times.append(f"Entire Chairs Scrape took: {elapsed_time:.2f} seconds")

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
print(f"Entire Sofas scrape took: {elapsed_time:.2f} seconds")
final_times.append(f"Entire Sofas Scrape took: {elapsed_time:.2f} seconds")

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

print("================================")
print("========Time elapsed============")
for stamp in final_times:
    print(stamp)


