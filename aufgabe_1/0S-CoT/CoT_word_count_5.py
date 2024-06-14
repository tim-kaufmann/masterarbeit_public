import string
from collections import Counter

def word_count(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        return {}

    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    # Split text into words
    words = text.split()

    # Count the words
    word_counts = Counter(words)

    # Sort the dictionary: first by count descending, then by word ascending
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))

    return sorted_word_counts
