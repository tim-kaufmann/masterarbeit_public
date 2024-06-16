import string
from collections import Counter

def word_count(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Remove punctuation and convert to lower case
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    
    # Split into words
    words = text.split()
    
    # Count the words
    word_counts = Counter(words)
    
    # Sort the words: first by frequency (descending), then alphabetically (ascending)
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))
    
    # Print the results
    for word, count in sorted_word_counts.items():
        print(f"'{word}': {count}")

    return sorted_word_counts
