from bs4 import BeautifulSoup
from collections import Counter
import re

def get_top_k_words_from_html(html, k):
    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    # Extract words and convert to lower case
    words = re.findall(r'\b\w+\b', text.lower())

    # Count word frequencies
    word_counts = Counter(words)

    # Get the top k words sorted by frequency and alphabetically for tie cases
    top_k_words = word_counts.most_common()
    top_k_words.sort(key=lambda x: (-x[1], x[0]))

    # Return only the top k words
    return top_k_words[:k]
