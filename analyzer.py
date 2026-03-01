# analyzer.py

import json
import os
import re
from collections import Counter
from logger import logger
from config import DATA_DIR


def find_repeated_words(titles):
    logger.info("Analyzing repeated words")

    words = []

    for title in titles:
        cleaned = re.sub(r"[^a-zA-Z ]", "", title.lower())
        words.extend(cleaned.split())

    counter = Counter(words)
    repeated = {word: count for word, count in counter.items() if count > 2}

    logger.info(f"Repeated words found: {repeated}")
    return repeated


def save_repeated_words(data):
    os.makedirs(DATA_DIR, exist_ok=True)
    path = f"{DATA_DIR}/repeated_words.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    logger.info(f"Repeated words saved to {path}")