import string
from collections import Counter

def word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove punctuation and make lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    # Split into words
    words = text.split()

    # Count words
    word_counts = Counter(words)

    # Sort by count (descending) and then alphabetically
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))

    # Print each word and its count
    for word, count in sorted_word_counts.items():
        print(f"'{word}': {count}")
