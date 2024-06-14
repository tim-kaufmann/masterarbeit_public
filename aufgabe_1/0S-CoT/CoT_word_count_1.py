import os
import string

def word_count(file_path):
    if not os.path.exists(file_path):
        return {}

    word_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().lower().translate(str.maketrans("", "", string.punctuation)).split()
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    sorted_word_dict = dict(sorted(word_dict.items(), key=lambda item: (-item[1], item[0])))

    return sorted_word_dict