from collections import Counter
from bs4 import BeautifulSoup
import re

def get_top_k_words_from_html(html, k):
    # Parse HTML content
    soup = BeautifulSoup(html, 'html.parser')
    # Get text from HTML
    text = soup.get_text()
    # Normalize to lower case and find all words
    words = re.findall(r'\b\w+\b', text.lower())
    # Count frequency of each word
    word_counts = Counter(words)
    # Get the most common k words
    top_k_words = word_counts.most_common(k)
    return top_k_words
