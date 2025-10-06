import requests
import pandas as pd
import time
import random

# -----------------------------------------
# CONFIG
# -----------------------------------------
headers = {
    "User-Agent": random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    ]),
    "Accept": "application/json",
}

# Example query: Toronto downtown region
base_url = "https://api.realtor.ca/Listing.svc/PropertySearch_Post"

payload = {
    "LongitudeMin": -79.50,
    "LongitudeMax": -79.35,
    "LatitudeMin": 43.63,
    "LatitudeMax": 43.68,
    "Sort": "6-D",
    "CultureId": 1,
    "ApplicationId": 1,
    "PropertySearchTypeId": 1,  # 1 = Residential
    "RecordsPerPage": 50,
    "CurrentPage": 1
}

# -----------------------------------------
# SCRAPE MULTIPLE PAGES
# -----------------------------------------
scraped_data = []
page = 1

while True:
    print(f"Fetching page {page}...")
    payload["CurrentPage"] = page
    response = requests.post(base_url, headers=headers, data=payload)
    data = response.json()

    results = data.get("Results", [])
    if not results:
        print("No more listings found.")
        break

    for item in results:
        building = item.get("Building", {})
        property_obj = item.get("Property", {})
        address = item.get("Property", {}).get("Address", {})

        scraped_data.append({
            "Price": item.get("Property", {}).get("Price"),
            "Address": address.get("AddressText"),
            "Beds": building.get("Bedrooms"),
            "Baths": building.get("BathroomTotal"),
            "Type": building.get("Type"),
            "SqFt": building.get("SizeInterior"),
            "Latitude": address.get("Latitude"),
            "Longitude": address.get("Longitude"),
            "MLS": item.get("MlsNumber"),
            "Link": f"https://www.realtor.ca/real-estate/{item.get('Id')}",
        })

    page += 1
    time.sleep(random.uniform(1, 3))  # respectful delay
    if page > 5:  # scrape first 5 pages only
        break

# -----------------------------------------
# SAVE TO CSV
# -----------------------------------------
df = pd.DataFrame(scraped_data)
save_path = "G:\\Desktop\\python-projects\\real_state_scrapping\\realtorca_api_toronto.csv"
df.to_csv(save_path, index=False, encoding="utf-8-sig")

print(f"\n✅ Scraping complete! {len(df)} listings saved to:\n{save_path}")
