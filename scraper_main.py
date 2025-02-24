from nordicnest_scraper import scrapeNordicnest
from chilli_scraper import scrapeChilli
import pandas as pd


def scrapeOptions():
    print("Scrape Products")
    print("Select one option")
    print("1. Scrape All")
    print("2. Scrape Nordicnest")
    print("3. Scrape Chilli")
    print("4. Back")

    
    while True:
        try:
            selected_option = int(input(""))

        except: 
            print("Invalid input, you must enter a number!")

        if selected_option >= 5 or selected_option <= 0:
            print("Options does not exist, select one from the list!")

        match selected_option:
            case 1:
                scrapeNordicnest()
                scrapeChilli()
                break
            case 2:
                scrapeNordicnest()
                break
            case 3:
                scrapeChilli()
                break
            case 4:
                break
        
def exportCsv():
    print("File exporter")
    print("Please select one of the options: ")
    print("1. Export all")
    print("2. Export tables")
    print("3. Export chairs")
    print("4. Export sofas")
    print("5. Back")  

    while True: 
        try:
            selected_option = int(input(""))
        except: 
            print("Invalid input, you must enter a number!")

        if selected_option >= 6 or selected_option <= 0:
            print("Options does not exist, select one from the list!")

        match selected_option:
            case 1:
                nordic_tables = pd.read_csv("nordicnest_tables.csv")
                chilli_tables = pd.read_csv("chilli_tables.csv")
                merged_tables = pd.concat([nordic_tables, chilli_tables], ignore_index=True)
                merged_tables.to_csv("all_tables.csv", index=False)

                nordic_chairs = pd.read_csv("nordicnest_chairs.csv")
                chilli_chairs = pd.read_csv("chilli_chairs.csv")
                merged_chairs = pd.concat([nordic_chairs, chilli_chairs], ignore_index=True)
                merged_chairs.to_csv("all_chairs.csv", index=False)

                nordic_sofas = pd.read_csv("nordicnest_sofas.csv")
                chilli_sofas = pd.read_csv("chilli_sofas.csv")
                merged_sofas = pd.concat([nordic_sofas, chilli_sofas], ignore_index=True)
                merged_sofas.to_csv("all_sofas.csv", index=False)
                print("All product categories has been exported to csv files!")
                break
            case 2: 
                nordic_tables = pd.read_csv("nordicnest_tables.csv")
                chilli_tables = pd.read_csv("chilli_tables.csv")
                merged_tables = pd.concat([nordic_tables, chilli_tables], ignore_index=True)
                merged_tables.to_csv("all_tables.csv", index=False)
                print("All tables has been exported to a csv file!")
                break
            case 3: 
                nordic_chairs = pd.read_csv("nordicnest_chairs.csv")
                chilli_chairs = pd.read_csv("chilli_chairs.csv")
                merged_chairs = pd.concat([nordic_chairs, chilli_chairs], ignore_index=True)
                merged_chairs.to_csv("all_chairs.csv", index=False)
                print("All chairs has been exported to a csv file!")
                break
            case 4:
                nordic_sofas = pd.read_csv("nordicnest_sofas.csv")
                chilli_sofas = pd.read_csv("chilli_sofas.csv")
                merged_sofas = pd.concat([nordic_sofas, chilli_sofas], ignore_index=True)
                merged_sofas.to_csv("all_sofas.csv", index=False)
                print("All sofas has been exported to a csv file!")
                break
            case 5:
                break


while True:
    print("Welcome to Lia Scraper, please select one of the options from the menu: ")
    print("1. Scrape Products")
    print("2. Export products to CSV files")
    print("3. Exit")

    try:
        selected_option = int(input(""))
    except ValueError:
        print("Invalid input, you must select a number!")

    if selected_option >= 4 or selected_option <= 0:
        print("Options does not exist, select one from the list!")
    match selected_option:
        case 1: 
            scrapeOptions()
        case 2:
            exportCsv()
        case 3:
            print("You selected the exit")
            exit()
