from collections import Counter
from bs4 import BeautifulSoup
import re

def get_top_k_words_from_html(html, k):
    # Parse the HTML content and extract the text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    
    # Normalize the text to lowercase and extract words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the top k words sorted by frequency and then alphabetically
    top_k_words = word_counts.most_common()
    top_k_words = sorted(top_k_words, key=lambda x: (-x[1], x[0]))
    
    return top_k_words[:k]

# Example usage (for demonstration purposes, not part of the function implementation):
# html_input = "<p>We are the world, we are the children.</p> <p>We are the ones who make a brighter day.</p> <p>So let's start giving.</p>"
# k = 3
# print(get_top_k_words_from_html(html_input, k))
