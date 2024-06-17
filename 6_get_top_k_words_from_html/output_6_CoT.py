from bs4 import BeautifulSoup
import re
from collections import Counter

def get_top_k_words_from_html(html, k):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract all text from the parsed HTML
    text = soup.get_text()
    
    # Convert text to lower case and find all words (a word is defined as a string composed of letters and numbers)
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Get the k most common words and their frequencies
    top_k_words = word_count.most_common(k)
    
    return top_k_words
