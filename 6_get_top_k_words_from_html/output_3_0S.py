from collections import Counter
from bs4 import BeautifulSoup
import re

def get_top_k_words_from_html(html, k):
    # Parse the HTML content and extract the text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    # Use regex to find all words (case insensitive)
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the frequency of each word
    word_count = Counter(words)

    # Get the most common words up to k
    top_k_words = word_count.most_common(k)

    return top_k_words
