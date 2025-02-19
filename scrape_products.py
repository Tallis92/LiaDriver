from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
 
tables = []
chairs = []
sofas = []
driver = webdriver.Firefox()

driver.get("https://www.nordicnest.se/")

cookies_accept = driver.find_element(By.ID, "acceptAllBtn")
cookies_accept.click()

# Adds table to products
driver.get("https://www.nordicnest.se/mobler/bord/matbord/")
anchor = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[6]/div[1]/ul/li[1]/div/a")
href = anchor.get_attribute("href")
anchor.click()

driver.implicitly_wait(5)
title = driver.find_element(By.XPATH, "//h1[contains(text(), 'S-table matbord')]").text
description = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div[1]/div/div").text
price = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[2]/div[3]/div/div[1]/span").text
image = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/img")
imgSrc = image.get_attribute("src")

table = [title, description, price, imgSrc, href]
tables.append(table)

driver.get("https://www.nordicnest.se/")
searchBtn = driver.find_element(By.XPATH, "//button[@aria-label='Sök']").click()
searchBar = driver.find_element(By.XPATH, "/html/body/div[3]/header/div/div[1]/form/div[1]/input")
searchBar.send_keys("stolar")
time.sleep(2)
searchBar.send_keys(Keys.RETURN)
time.sleep(1)

anchor = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[6]/div[1]/ul/li[1]/div/a")
href = anchor.get_attribute("href")
anchor.click()


# Adds chair to products
driver.implicitly_wait(5)
title = driver.find_element(By.XPATH, "//h1[contains(text(), 'Cover sidostol')]").text
description = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div[1]/div/div").text
price = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[2]/div[3]/div/div[1]/span").text
image = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/img")
imgSrc = image.get_attribute("src")

chair = [title, description, price, imgSrc, href]
chairs.append(chair)

# Adds another chair to products
driver.back()
anchor = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[6]/div[1]/ul/li[10]/div/a")
href = anchor.get_attribute("href")
anchor.click()

# Adds chair to products
driver.implicitly_wait(5)
title = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[1]/h1").text
description = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div[1]/div/div").text
price = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[2]/div[3]/div/div[1]/span").text
image = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/img")
imgSrc = image.get_attribute("src")

chair = [title, description, price, imgSrc, href]
chairs.append(chair)

# Adds sofa to products
driver.get("https://www.nordicnest.se/mobler/soffor--fatoljer/soffor/")
driver.implicitly_wait(5)
anchor = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[7]/div[1]/ul/li[17]/div/a")
driver.execute_script("arguments[0].scrollIntoView();", anchor)
WebDriverWait(driver, 10).until(EC.visibility_of(anchor))
href = anchor.get_attribute("href")
anchor.click()

driver.implicitly_wait(5)
title = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[1]/h1").text
description = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div[1]/div/div").text
price = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[2]/div[3]/div/div[1]/span").text
image = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/img")
imgSrc = image.get_attribute("src")

sofa = [title, description, price, imgSrc, href]
sofas.append(sofa)

driver.back()
anchor = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[7]/div[1]/ul/li[13]/div/a")
href = anchor.get_attribute("href")
anchor.click()

driver.implicitly_wait(5)
title = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[1]/h1").text
description = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div[1]/div/div").text
price = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[2]/div[2]/div[3]/div/div[1]/span").text
image = driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/img")
imgSrc = image.get_attribute("src")

sofa = [title, description, price, imgSrc, href]
sofas.append(sofa)


# Changes site to search for products
driver.get("https://www.chilli.se/inredning")

cookies_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
driver.get("https://www.chilli.se/m%C3%B6bler/bord/soffbord")
anchor = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[2]/ul/li[2]/div/a") #div[2]/h2"
href = anchor.get_attribute("href")
anchor.click()

title = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/h1").text
reveal_text = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/h3/span").click()
driver.implicitly_wait(5)

description = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/div/div/p[1]").text
price = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div/span[2]").text
image = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div/div[2]/div[1]/div/div/div[1]/img")
imgSrc = image.get_attribute("src")

table = [title, description, price, imgSrc, href]
tables.append(table)

driver.back()
anchor = driver.find_element(By.XPATH, "//h2[contains(text(), 'Soffbord Hammarstrand 100 cm')]")
href = anchor.get_attribute("href")
anchor.click()
title = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/h1").text
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/h3/span").click()
    driver.implicitly_wait(5)
    description = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/div/div/p[1]").text
except NoSuchElementException:
    print("There was no product description!")
    description = "No description exists for this product..."

price = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div/span[2]").text
image = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div/div[2]/div[1]/div/div/div[1]/img")
imgSrc = image.get_attribute("src")

table = [title, description, price, imgSrc, href]
tables.append(table)

driver.get("https://www.chilli.se/m%C3%B6bler/stolar/matstolar-k%C3%B6ksstolar")
anchor = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[2]/ul/li[10]/div/a")
href = anchor.get_attribute("href")
anchor.click()

driver.implicitly_wait(5)
title = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/h1").text
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/h3/span").click()
    driver.implicitly_wait(5)
    description = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/div/div/p[1]").text
except NoSuchElementException:
    print("There was no product description!")
    description = "No description exists for this product..."
driver.implicitly_wait(5)

price = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div/span[2]").text
image = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div/div[2]/div[1]/div/div/div[1]/img")
imgSrc = image.get_attribute("src")

chair = [title, description, price, imgSrc, href]
chairs.append(chair)


driver.get("https://www.chilli.se/m%C3%B6bler/soffor/4-sits-soffa")
anchor = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/div[2]/ul/li[10]/div/a")
href = anchor.get_attribute("href")
anchor.click()

driver.implicitly_wait(5)
title = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/h1").text
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/h3/span").click()
    driver.implicitly_wait(5)
    description = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[4]/div/div[1]/div[3]/div/div/p[1]").text
except NoSuchElementException:
    print("There was no product description!")
    description = "No description exists for this product..."
driver.implicitly_wait(5)

price = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div[1]/div[1]/div[2]/span[2]").text
image = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div/div[2]/div[1]/div/div/div[1]/img")
imgSrc = image.get_attribute("src")

sofa = [title, description, price, imgSrc, href]
sofas.append(sofa)
# gets products from sleepo.se
# driver.get("https://www.sleepo.se/inredning/")
# driver.implicitly_wait(3)
# cookies_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

# driver.get("https://www.sleepo.se/mobler/soffor-fatoljer/soffor/")
# driver.implicitly_wait(3)
# driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[3]/div/div/div[1]/div/div[1]/div/div/div[2]/section/div/ul/li[1]/article/div[3]/header/a").click()

# driver.implicitly_wait(5)
# title = driver.find_element(By.XPATH, "//h1[contains(text(), 'Blanca 3-sits Divansoffa Forest')]").text
# description = driver.find_element(By.ID, "collapse0").text
# price = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div[2]/div/div[2]/span").text
# product5 = [title, description, price]
# products.append(product5)

# Writes every product into a csv file
with open('scraped_tables.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for table in tables:
        writer.writerow(table)
print("\033[92mData saved to scraped_tables.csv!\033[0m")

with open('scraped_chairs.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for chair in chairs:
        writer.writerow(chair)
print("\033[92mData saved to scraped_chairs.csv!\033[0m")

with open('scraped_sofas.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for sofa in sofas:
        writer.writerow(sofa)
print("\033[92mData saved to scraped_chairs.csv!\033[0m")

driver.quit()