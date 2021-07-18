from typing import List

def slices(series: str, length: int) -> List[str]:

    if length > len(series):
        raise ValueError(
            "substring length can't be greater than string length"
        )
    if length <= 0:
        raise ValueError(
            "substring length must be a positive integer"
        )

    i = 0
    j = length
    substrings = []
    while j <= len(series):
        substrings.append(series[i:j])
        i += 1
        j += 1
    
    return substrings

