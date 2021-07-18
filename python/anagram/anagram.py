def find_anagrams(word, candidates):

    letter_count = {}
    for letter in word.lower():
        letter_count[letter] = letter_count.get(letter, 0) + 1

    anagrams = []
    for candidate in candidates:
        if len(candidate) != len(word): continue
        if candidate.lower() == word.lower(): continue
        
        is_anagram = True
        candidate_count = letter_count.copy()
        for letter in candidate.lower():
            if not candidate_count.get(letter):
                is_anagram = False
                break
            else:
                candidate_count[letter] -= 1
        if is_anagram:
            anagrams.append(candidate)

    return anagrams
