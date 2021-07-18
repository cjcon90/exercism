import re

ISBN_REG = re.compile("\\d{1}[-]?\\d{3}[-]?\\d{5}[-]?[\\d|X]")

def is_valid(isbn:str) -> bool:
    
    if not ISBN_REG.fullmatch(isbn):
        return False

    total = 0
    multiplier = 10
    total = 0
    for char in isbn:
        if char == '-':
            continue
        num = 10 if char is 'X' else int(char)
        total += (multiplier * num)
        multiplier -= 1

    return total % 11 == 0
