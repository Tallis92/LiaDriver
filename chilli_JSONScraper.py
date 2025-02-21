import csv
import requests
from bs4 import BeautifulSoup

# Definiera kategorier och deras API-endpoints
categories = {
    "chilli_sofas_JSON": "https://www.chilli.se/api/content/m%C3%B6bler/soffor",
    "chilli_chairs_JSON": "https://www.chilli.se/api/content/m%C3%B6bler/stolar",
    "chilli_tables_JSON": "https://www.chilli.se/api/content/m%C3%B6bler/bord"
}

# Hämta och processa data för varje kategori
for category, base_url in categories.items():
    # Skapar filnamn baserat på kategorin (soffor.csv, bord.csv, osv.)
    filename = f"{category.lower()}.csv"  

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Description", "Price", "Discount", "Href", "Image URL"])

        # Loopar igenom sidorna 1-3
        for page in range(1, 4):  
            json_url = f"{base_url}?page={page}" 
            response = requests.get(json_url, headers={"User-Agent": "Mozilla/5.0"})

            if response.status_code == 200:
                data = response.json()

                for product in data.get("products", []):
                    name = product.get("displayName", "Ej angivet")
                    price = product.get("price", {}).get("current", {}).get("inclVat", "Ej angivet")
                    discount = product.get("price", {}).get("discount", "Ej angivet")
                    href = "https://www.chilli.se" + product.get("url", "")
                    image_url = "https://www.chilli.se" + product.get("images", [{}])[0].get("url", "")

                    # Hämta produktbeskrivning från produktsidan
                    try:
                        product_page = requests.get(href, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
                        product_page.raise_for_status()

                        soup = BeautifulSoup(product_page.text, "html.parser")

                        # Hitta den längsta <p>-taggen på sidan
                        paragraphs = soup.find_all("p")
                        longest_paragraph = max(paragraphs, key=lambda p: len(p.text.strip()), default=None)
                        description = longest_paragraph.text.strip() if longest_paragraph else "Ej angivet"

                    except requests.RequestException:
                        description = "Ej angivet"
                    except Exception:
                        description = "Ej angivet"

                    writer.writerow([name, description, price, discount, href, image_url])

            print(f"Klar med {category} - Sida {page}")

    print(f"{filename} har sparats!")

print("Alla kategorier har sparats!")

