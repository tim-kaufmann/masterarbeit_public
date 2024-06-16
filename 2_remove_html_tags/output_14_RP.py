import string
from collections import Counter

def word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words and count
    words = text.split()
    word_counts = Counter(words)
    
    # Sort the dictionary
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))
    
    for word, count in sorted_word_counts.items():
        print(f"'{word}': {count}")

# Example usage:
# word_count('path_to_your_file.txt')
