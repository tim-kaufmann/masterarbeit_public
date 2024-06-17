import re
from collections import Counter
from bs4 import BeautifulSoup

def get_top_k_words_from_html(html, k):
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract text from HTML
    text = soup.get_text()
    
    # Normalize the text to lowercase and find all words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the k most common words
    top_k_words = word_counts.most_common(k)
    
    return top_k_words
