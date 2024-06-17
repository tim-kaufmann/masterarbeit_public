import re
from collections import Counter
from bs4 import BeautifulSoup

def get_top_k_words_from_html(html, k):
    # Parse the HTML content and extract text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    
    # Use regex to find words and convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the top k words sorted by frequency and then alphabetically
    most_common_words = word_counts.most_common()
    most_common_words.sort(key=lambda x: (-x[1], x[0]))
    
    return most_common_words[:k]
