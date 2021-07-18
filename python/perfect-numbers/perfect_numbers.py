def classify(number:int) -> str:

    if number <= 0:
        raise ValueError("Positive integer must be provided")

    aliquot = 1
    i = 2
    j = int(number / 2)
    while i < j:
        if number % i == 0:
            j = int(number / i)
            aliquot += (i + j)
        i += 1

    
    if aliquot == 1 or aliquot < number:
        return "deficient"
    elif aliquot > number:
        return "abundant"
    else:
        return "perfect"
