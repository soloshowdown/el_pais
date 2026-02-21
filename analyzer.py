import json
from collections import Counter
import os
import logging

logger = logging.getLogger(__name__)

def save_repeated_words(words, min_count=2):
    counter = Counter(words)
    repeated = {word: count for word, count in counter.items() if count > min_count}

    os.makedirs("output", exist_ok=True)

    with open("output/repeated_words.json", "w", encoding="utf-8") as f:
        json.dump(repeated, f, indent=4, ensure_ascii=False)

    logger.info("Repeated words saved to output/repeated_words.json")