def is_pangram(sentence):
    found = {}
    for char in sentence:
        if char.isalpha():
            code = ord(char.lower())
            found[code] = found.get(code, 0) + 1

    return len(found) == 26
