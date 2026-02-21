import os
from scraper import scrape_articles
from translator import translate_text
from analyzer import find_repeated_words, save_repeated_words


def main():
    os.makedirs("output/images", exist_ok=True)
    os.makedirs("output/data", exist_ok=True)

    print("\nStarting El País Opinion Scraper\n")

    articles = scrape_articles(limit=5)

    translated_titles = []

    for idx, article in enumerate(articles, start=1):
        print(f"\nARTICLE {idx}")
        print("TITLE (ES):", article["title"])
        print("CONTENT (ES):", article["content"][:800], "...\n")

        translated = translate_text(article["title"])
        translated_titles.append(translated)

        print("TITLE (EN):", translated)

    repeated_words = find_repeated_words(translated_titles)
    save_repeated_words(repeated_words)

    print("\nREPEATED WORDS (>2 times):")
    for word, count in repeated_words.items():
        print(f"{word} → {count}")

    print("\nExecution completed successfully")


if __name__ == "__main__":
    main()