from collections import Counter
from bs4 import BeautifulSoup
import re

def get_top_k_words_from_html(html, k):
    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    # Extract words and convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the frequency of each word
    word_count = Counter(words)

    # Get the top k words sorted by frequency and alphabetically for ties
    most_common = word_count.most_common()
    most_common.sort(key=lambda x: (-x[1], x[0]))

    return most_common[:k]
