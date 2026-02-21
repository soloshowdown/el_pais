import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from scraper import scrape_article, handle_cookies
from translator import translate_text
from analyzer import save_repeated_words

# ---------------- LOGGING ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# ---------------- SETUP DRIVER ----------------
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

BASE_URL = "https://elpais.com/opinion/"

# ---------------- SCRAPING ----------------
driver.get(BASE_URL)
handle_cookies(driver)

article_links = []
articles = driver.find_elements("css selector", "article h2 a")

for a in articles[:5]:
    link = a.get_attribute("href")
    if link:
        article_links.append(link)

titles_es = []
titles_en = []
all_words = []

for idx, link in enumerate(article_links, start=1):
    title_es, content_es = scrape_article(driver, link)

    print(f"\nARTICLE {idx}")
    print(f"TITLE (ES): {title_es}")
    print(f"CONTENT (ES): {content_es[:300]}...")

    title_en = translate_text(title_es)

    titles_es.append(title_es)
    titles_en.append(title_en)

    all_words.extend(title_en.lower().split())

# ---------------- RESULTS ----------------
print("\nTRANSLATED TITLES (EN):")
for t in titles_en:
    print("-", t)

save_repeated_words(all_words)

driver.quit()
logger.info("Execution completed successfully")