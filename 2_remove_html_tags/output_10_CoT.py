import string
from collections import Counter

def word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Sort the dictionary by count in descending order, then alphabetically
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))
    
    # Print the sorted dictionary
    for word, count in sorted_word_counts.items():
        print(f"'{word}': {count}")

