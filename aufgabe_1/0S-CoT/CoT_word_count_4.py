import os
import string
from collections import Counter

def word_count(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
        # Normalize the text: lower case and remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        normalized_text = text.lower().translate(translator)
        
        # Split the text into words
        words = normalized_text.split()
        
        # Count the words
        word_counts = Counter(words)
        
        # Sort the dictionary: first by count descending, then alphabetically
        sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: (-item[1], item[0])))
        
        return sorted_word_counts
    except FileNotFoundError:
        return {}

