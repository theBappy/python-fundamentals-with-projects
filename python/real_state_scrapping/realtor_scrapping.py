from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import time
import random

# -----------------------------------------
# SETTINGS
# -----------------------------------------
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/119.0",
]

profile_path = "C:\\Users\\User\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\j47zrpxa.myself"

options = Options()
options.profile = FirefoxProfile(profile_path)
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)
options.set_preference("general.useragent.override", random.choice(USER_AGENTS))

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

# -----------------------------------------
# SCRAPING CONFIG
# -----------------------------------------
base_url = "https://www.realtor.ca/map#ZoomLevel=11&Center=43.653963,-79.387207"
scraped_data = []

driver.get(base_url)
time.sleep(random.uniform(6, 9))

print(f"Page title: {driver.title}")
if "Access" in driver.title or "blocked" in driver.page_source.lower():
    print("WARNING: Site blocked the request!")
    driver.quit()
    exit()

# -----------------------------------------
# SCRAPING LOOP
# -----------------------------------------
page_number = 1
while True:
    print(f"\nScraping page {page_number}...")

    # Try locating listing cards
    listings = driver.find_elements("css selector", "div.smallListingCard")
    if not listings:
        print("No listings found on this page.")
        break

    print(f"Found {len(listings)} listings.")

    for card in listings:
        try:
            price = card.find_element("css selector", "div.smallListingCardPrice").text.strip()
        except:
            price = "N/A"

        try:
            address = card.find_element("css selector", "div.smallListingCardAddress").text.strip()
        except:
            address = "N/A"

        try:
            beds = card.find_element("css selector", "div.smallListingCardIconCon").text.strip()
        except:
            beds = "N/A"

        try:
            baths = card.find_element("css selector", "div.smallListingCardIconText").text.strip()
        except:
            baths = "N/A"

        try:
            sqft = card.find_element("css selector", "div.smallListingCardIconNum").text.strip()
        except:
            sqft = "N/A"


        try:
            image = card.find_element("css selector", "img.smallListingCardImage").get_attribute("src")
        except:
            image = "N/A"

        scraped_data.append({
            "Price": price,
            "Address": address,
            "Beds": beds,
            "Baths": baths,
            "SqFt": sqft,
            "Image URL": image
        })

    # Pagination (realtor.ca uses scroll or "next" button)
    try:
        next_btn = driver.find_element("css selector", "a.pagination__link--next")
        next_href = next_btn.get_attribute("href")
        if next_href:
            driver.get(next_href)
            page_number += 1
            time.sleep(random.uniform(6, 10))
        else:
            print("No next page link found.")
            break
    except:
        print("No next page found. Scraping complete.")
        break

# -----------------------------------------
# SAVE CSV
# -----------------------------------------
df = pd.DataFrame(scraped_data)
save_path = "G:\\Desktop\\python-projects\\real_state_scrapping\\realtorca_toronto.csv"
df.to_csv(save_path, index=False, encoding='utf-8-sig')

print(f"\n✅ Scraping complete! {len(df)} listings saved to:\n{save_path}")

driver.quit()
