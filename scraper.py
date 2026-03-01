
import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from logger import logger
from config import BASE_URL, IMAGE_DIR, PAGE_LOAD_WAIT


def scrape_articles(limit=5):
    logger.info("Starting scraper")

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)

    time.sleep(PAGE_LOAD_WAIT)

    articles = []

    article_links = driver.find_elements(By.CSS_SELECTOR, "article a")[:limit]
    urls = [a.get_attribute("href") for a in article_links if a.get_attribute("href")]

    logger.info(f"Found {len(urls)} article URLs")

    for idx, url in enumerate(urls, start=1):
        logger.info(f"Scraping article {idx}: {url}")

        driver.get(url)
        time.sleep(PAGE_LOAD_WAIT)

        title = extract_title(driver)
        content = extract_content(driver)
        image_downloaded = download_cover_image(driver, idx)

        articles.append({
            "title": title,
            "content": content,
            "image_downloaded": image_downloaded
        })

    driver.quit()
    logger.info("Scraping completed")

    return articles


def extract_title(driver):
    try:
        return driver.find_element(By.TAG_NAME, "h1").text
    except:
        logger.warning("H1 not found, trying H2")
        try:
            return driver.find_element(By.TAG_NAME, "h2").text
        except:
            logger.error("Title not found")
            return "No title"


def extract_content(driver):
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
    text = " ".join(p.text for p in paragraphs if p.text.strip())

    if not text:
        logger.warning("Article content empty")

    return text or "No content"


def download_cover_image(driver, idx):
    try:
        img = driver.find_element(By.CSS_SELECTOR, "figure img")
        img_url = img.get_attribute("src")

        if not img_url:
            logger.warning("Image src empty")
            return False

        response = requests.get(img_url, timeout=10)
        response.raise_for_status()

        os.makedirs(IMAGE_DIR, exist_ok=True)
        path = f"{IMAGE_DIR}/article_{idx}.jpg"

        with open(path, "wb") as f:
            f.write(response.content)

        logger.info(f"Image saved: {path}")
        return True

    except Exception as e:
        logger.warning(f"Image download failed: {e}")
        return False