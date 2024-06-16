import string
from collections import Counter

def word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove punctuation and convert to lower case
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Sort the dictionary by count descending and then by word ascending
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))

    # Print the sorted dictionary
    for word, count in sorted_word_counts.items():
        print(f"'{word}': {count}")

# Example usage (This line should not be included in the final code block)
# word_count('path_to_file.txt')
