import string
from collections import Counter

def word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Remove punctuation and make lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Count the words
    word_counts = Counter(words)
    
    # Sort the dictionary
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))
    
    # Print the sorted word counts
    for word, count in sorted_word_counts.items():
        print(f"'{word}': {count}")