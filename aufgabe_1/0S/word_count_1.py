import os
import string
from collections import Counter

def word_count(file_path):
    if not os.path.exists(file_path):
        return {}

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split the text into words
    words = text.split()

    # Count the words
    word_counts = Counter(words)
    
    # Sort the dictionary by count (descending) and then alphabetically
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))

    # Print the results as required by the test
    for word, count in sorted_word_counts.items():
        print(f"'{word}': {count}")

    return sorted_word_counts
