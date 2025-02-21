import csv
import requests

json_url = "https://www.chilli.se/api/content/m%C3%B6bler/soffor"

response = requests.get(json_url)

if response.status_code == 200:
    data = response.json()

    with open("soffor.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(["Namn", "Pris", "Länk"])

        for product in data.get("products", []):
            namn = product.get("displayName", "Ej angivet")
            pris = product.get("price", {}).get("current", {}).get("inclVat", "Ej angivet")
            description = product.get("description", "Ej angivet")
            rabatt = product.get("price", {}).get("discount", "Ej angivet")
            länk = "https://www.chilli.se" + product.get("url", "")
            #bild = "https://www.chilli.se" + product.get("images", [{}])[0].get("url", "")

            writer.writerow([namn, pris, description, rabatt, länk])

    print("Alla produkter har sparats i 'soffor.csv'")
else:
    print(f"Misslyckades att hämta JSON-data (statuskod {response.status_code})")
