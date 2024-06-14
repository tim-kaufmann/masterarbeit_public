import os
import string
from collections import Counter

def word_count(file_path):
    if not os.path.isfile(file_path):
        return {}

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
    
    word_counter = Counter(words)
    sorted_word_count = dict(sorted(word_counter.items(), key=lambda item: (-item[1], item[0])))
    
    for word, count in sorted_word_count.items():
        print(f"'{word}': {count}")
    
    return sorted_word_count
