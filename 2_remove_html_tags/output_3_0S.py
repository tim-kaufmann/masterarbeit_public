import string
from collections import Counter

def word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove punctuation and make all words lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()

    # Split the text into words
    words = cleaned_text.split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Sort the words by count (descending) and alphabetically (ascending) for ties
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))

    # Print the sorted word counts
    for word, count in sorted_word_counts.items():
        print(f"'{word}': {count}")

# Example usage
# word_count('path_to_your_file.txt')
