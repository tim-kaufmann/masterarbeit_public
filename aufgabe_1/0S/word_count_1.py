import string
from collections import Counter


def word_count(file_path):
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 移除标点符号并转换为小写
        translator = str.maketrans("", "", string.punctuation)
        content = content.translate(translator).lower()

        # 使用 Counter 统计单词出现次数
        words = content.split()
        word_counter = Counter(words)

        # 按照出现次数降序排列
        sorted_word_count = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)

        for word, count in sorted_word_count:
            print(f"'{word}': {count}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
