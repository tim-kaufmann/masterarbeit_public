from collections import Counter
from bs4 import BeautifulSoup
import re

def get_top_k_words_from_html(html, k):
    # Remove HTML tags using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    
    # Convert text to lowercase and find all words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the top k words sorted by frequency and then alphabetically
    top_k_words = word_counts.most_common()
    
    # Sort words with the same frequency alphabetically
    sorted_top_k_words = sorted(top_k_words, key=lambda x: (-x[1], x[0]))
    
    # Return only the top k words
    return sorted_top_k_words[:k]
