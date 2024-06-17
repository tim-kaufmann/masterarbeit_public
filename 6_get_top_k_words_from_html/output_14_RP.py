from bs4 import BeautifulSoup
from collections import Counter
import re

def get_top_k_words_from_html(html, k):
    # Parse HTML content and extract text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    
    # Convert text to lower case and extract words using regular expression
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Get the top k words by frequency, sorted in descending order
    top_k_words = word_count.most_common(k)
    
    return top_k_words
