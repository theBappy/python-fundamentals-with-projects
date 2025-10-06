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
# SCRAPE FROM STATIC TRAINING SITE
# -----------------------------------------
base_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
scraped_data = []

driver.get(base_url)
time.sleep(random.uniform(4, 6))
print(f"Page title: {driver.title}")

page_number = 1
while True:
    print(f"\nScraping page {page_number}...")

    listings = driver.find_elements("css selector", "div.thumbnail")
    print(f"Found {len(listings)} listings on this page.")

    for card in listings:
        try:
            title = card.find_element("css selector", "a.title").text.strip()
        except:
            title = "N/A"

        try:
            price = card.find_element("css selector", "h4.price").text.strip()
        except:
            price = "N/A"

        try:
            description = card.find_element("css selector", "p.description").text.strip()
        except:
            description = "N/A"

        try:
            reviews = card.find_element("css selector", "p.pull-right").text.strip()
        except:
            reviews = "N/A"

        try:
            link = card.find_element("css selector", "a.title").get_attribute("href")
        except:
            link = "N/A"

        scraped_data.append({
            "Title": title,
            "Price": price,
            "Description": description,
            "Reviews": reviews,
            "Link": link
        })

    # Check pagination (if exists)
    try:
        next_button = driver.find_element("css selector", "ul.pagination li:last-child a")
        next_href = next_button.get_attribute("href")
        if next_href and "page=" in next_href:
            print("Going to next page...")
            driver.get(next_href)
            page_number += 1
            time.sleep(random.uniform(4, 7))
        else:
            print("No more pages found.")
            break
    except:
        print("No next page found. Scraping complete.")
        break

# -----------------------------------------
# SAVE DATA
# -----------------------------------------
df = pd.DataFrame(scraped_data)
save_path = "G:\\Desktop\\python-projects\\real_state_scrapping\\training_site_laptops.csv"
df.to_csv(save_path, index=False, encoding='utf-8-sig')

print(f"\n✅ Scraping complete! {len(df)} items saved to:\n{save_path}")

driver.quit()
