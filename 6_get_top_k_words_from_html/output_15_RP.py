from collections import Counter
from bs4 import BeautifulSoup
import re

def get_top_k_words_from_html(html, k):
    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    # Get the text content from the HTML
    text = soup.get_text()
    # Use regex to find all words (alphanumeric strings) and convert them to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    # Count the frequency of each word
    word_counts = Counter(words)
    # Get the top k words with their frequencies
    top_k_words = word_counts.most_common(k)
    return top_k_words
