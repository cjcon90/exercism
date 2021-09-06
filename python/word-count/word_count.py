import re
from collections import Counter

def count_words(sentence: str) -> dict:
    word_reg = "[a-z]+'[a-z]+|[a-z0-9]+"
    return Counter(re.findall(word_reg, sentence.lower()))
