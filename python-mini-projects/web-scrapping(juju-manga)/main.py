import os
import re
import requests
from zipfile import ZipFile
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_latest_chapter_link():
    """Fetch the latest Jujutsu Kaisen manga chapter link from jujmanga.com (headless)."""
    print("[1/5] Launching Chrome in headless mode...")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    url = "https://jujmanga.com"
    pattern = r"/manga/"

    print("[2/5] Loading website and collecting manga links...")
    driver.get(url)
    links = driver.find_elements(By.TAG_NAME, "a")
    chapter_links = []

    for l in links:
        link = l.get_attribute("href")
        if isinstance(link, str) and re.search(pattern, link):
            chapter_links.append(link)

    driver.quit()

    chapter_links = sorted(set(chapter_links))

    if not chapter_links:
        raise Exception("❌ No chapter links found!")

    # Extract chapter numbers and pick the highest one
    def extract_chapter_num(link):
        match = re.search(r"chapter-(\d+)", link)
        return int(match.group(1)) if match else 0

    latest_chapter = max(chapter_links, key=extract_chapter_num)
    chapter_num = extract_chapter_num(latest_chapter)

    print(f"[3/5] ✅ Latest chapter found: Chapter {chapter_num}")
    print(f"URL: {latest_chapter}")

    with open("latest_chapter.txt", "w", encoding="utf-8") as f:
        f.write(latest_chapter)

    print("[4/5] Saved latest chapter link to latest_chapter.txt")
    return latest_chapter


def scrape_chapter(chapter_url):
    """Download all images from the chapter page."""
    match = re.search(r"chapter-(\d+)", chapter_url)
    chapter_num = int(match.group(1)) if match else 1
    folder_name = f"chapter_{chapter_num}"

    os.makedirs(folder_name, exist_ok=True)
    print(f"\n[Downloading Chapter {chapter_num}]")

    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(chapter_url.strip(), headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    images = soup.find_all("img")

    total = len(images)
    print(f"Found {total} images. Downloading...")

    for i, image in enumerate(images):
        src = image.get("src")
        if src and src.startswith("https") and "jujmanga" in src:
            fname = f"{folder_name}/{folder_name}_{i}.jpg"
            req = Request(url=src, headers=headers)
            try:
                with open(fname, "wb") as f:
                    f.write(urlopen(req).read())
                print(f"  ✅ Image {i+1}/{total}")
            except Exception as e:
                print(f"  ⚠️ Failed to download image {i+1}: {e}")

    print(f"\n✅ Chapter {chapter_num} images downloaded successfully!")
    return chapter_num


def zip_chapter(chapter_num):
    """Zip all downloaded images into a CBZ file."""
    output_file = f"Jujutsu_Kaisen_Chapter_{chapter_num}.cbz"
    with ZipFile(output_file, "w") as zipf:
        for root, _, files in os.walk(f"./chapter_{chapter_num}"):
            for f in files:
                if f.endswith(".jpg"):
                    file_path = os.path.join(root, f)
                    zipf.write(file_path)
                    print(f"Zipping {file_path}")
    print(f"✅ Zipped into {output_file}")


if __name__ == "__main__":
    # Step 1: Get latest chapter link
    if not os.path.exists("latest_chapter.txt"):
        chapter_url = get_latest_chapter_link()
    else:
        with open("latest_chapter.txt", "r", encoding="utf-8") as f:
            chapter_url = f.read().strip()

    # Step 2: Scrape and download that chapter
    chapter_num = scrape_chapter(chapter_url)

    # Step 3: Zip it into a CBZ file
    zip_chapter(chapter_num)
