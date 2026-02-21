import json
import os
import re
from collections import Counter


def find_repeated_words(titles):
    words = []

    for title in titles:
        cleaned = re.sub(r"[^a-zA-Z ]", "", title.lower())
        words.extend(cleaned.split())

    counter = Counter(words)
    return {word: count for word, count in counter.items() if count > 2}


def save_repeated_words(data, path="output/data/repeated_words.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)