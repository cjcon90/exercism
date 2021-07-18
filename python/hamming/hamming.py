def distance(strand_a:str, strand_b:str) -> int:
    
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length")
    else:
        hamming_distance = 0
        for index, letter in enumerate(strand_a):
            if letter != strand_b[index]:
                hamming_distance += 1

    return hamming_distance
