import re
from collections import Counter
from bs4 import BeautifulSoup

def get_top_k_words_from_html(html, k):
    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    
    # Normalize text to lowercase and extract words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the top k words sorted by frequency
    top_k_words = word_counts.most_common(k)
    
    return top_k_words
