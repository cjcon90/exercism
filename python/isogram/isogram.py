import re

def is_isogram(string:str) -> bool:
    test_str = re.sub("[^a-z]", "", string.lower()) 
    return len(test_str) == len(set(list(test_str)))
