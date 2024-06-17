import re
from collections import Counter
from bs4 import BeautifulSoup

def get_top_k_words_from_html(html, k):
    # Parse the HTML to extract text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    
    # Convert text to lowercase and find all words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the most common words and their frequencies
    common_words = word_counts.most_common()
    
    # Collect the top k words and frequencies, including ties
    result = []
    rank = 0
    prev_count = None
    
    for word, count in common_words:
        if rank < k or count == prev_count:
            result.append((word, count))
            if count != prev_count:
                rank += 1
                prev_count = count
        else:
            break
    
    return result
