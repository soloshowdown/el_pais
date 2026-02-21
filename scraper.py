import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def scrape_articles(limit=5):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.get("https://elpais.com/opinion/")

    time.sleep(3)

    articles = []
    links = driver.find_elements(By.CSS_SELECTOR, "article a")[:limit]

    urls = [link.get_attribute("href") for link in links if link.get_attribute("href")]

    for idx, url in enumerate(urls, start=1):
        driver.get(url)
        time.sleep(3)

        try:
            title = driver.find_element(By.TAG_NAME, "h1").text
        except:
            title = "No title"

        try:
            paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
            content = " ".join([p.text for p in paragraphs if p.text.strip()])
        except:
            content = "No content"

        image_downloaded = download_cover_image(driver, idx)

        articles.append({
            "title": title,
            "content": content,
            "image_downloaded": image_downloaded
        })

    driver.quit()
    return articles


def download_cover_image(driver, idx):
    try:
        img = driver.find_element(By.CSS_SELECTOR, "figure img")
        img_url = img.get_attribute("src")

        if not img_url:
            return False

        response = requests.get(img_url, timeout=10)
        if response.status_code == 200:
            path = f"output/images/article_{idx}.jpg"
            with open(path, "wb") as f:
                f.write(response.content)
            return True

    except:
        pass

    return False