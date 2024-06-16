import string
from collections import Counter

def word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Convert to lower case and remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    words = text.lower().translate(translator).split()

    # Count words
    word_counts = Counter(words)

    # Sort by frequency (descending) and alphabetically
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))

    for word, count in sorted_word_counts.items():
        print(f"'{word}': {count}")

