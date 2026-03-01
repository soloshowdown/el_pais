import os
from scraper import scrape_articles
from translator import translate_text
from analyzer import find_repeated_words, save_repeated_words
from logger import logger


def main():
    os.makedirs("output/images", exist_ok=True)
    os.makedirs("output/data", exist_ok=True)

    logger.info("Starting El País Opinion Scraper")

    articles = scrape_articles(limit=5)
    logger.info(f"Fetched {len(articles)} articles")

    translated_titles = []

    for idx, article in enumerate(articles, start=1):
        logger.info(f"Processing article {idx}")

        logger.info(f"Title (ES): {article['title']}")
        logger.debug(f"Content (ES): {article['content'][:800]}")

        translated = translate_text(article["title"])
        translated_titles.append(translated)

        logger.info(f"Title (EN): {translated}")

    repeated_words = find_repeated_words(translated_titles)
    save_repeated_words(repeated_words)

    logger.info("Repeated words analysis completed")

    for word, count in repeated_words.items():
        logger.info(f"{word} → {count}")

    logger.info("Execution completed successfully")


if __name__ == "__main__":
    main() 