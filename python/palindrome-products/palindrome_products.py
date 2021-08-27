def is_valid_test(min, max):
    if min > max:
        raise ValueError("Error: Minimum factor is lower than Maximum.")

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def smallest(min_factor, max_factor):
    is_valid_test(min_factor,max_factor)
    i = min_factor
    palindrome = 0
    factors = []
    while i < max_factor:
        j = i
        while j <= max_factor:
            product = i * j
            if palindrome and product > palindrome:
                j = max_factor
            if is_palindrome(product):
                if product < palindrome or not palindrome:
                    palindrome = product
                    factors = [[i, j]]
                elif product == palindrome:
                    factors.append([i, j])
                j = max_factor
            j = j + 1
        i = i + 1
    return palindrome if palindrome else None, factors

def largest(min_factor, max_factor):
    is_valid_test(min_factor,max_factor)
    i = max_factor
    palindrome = 0
    factors = []
    while i > min_factor:
        j = i
        while j >= min_factor:
            product = i * j
            if palindrome and product < palindrome:
                j = 0
            if is_palindrome(product):
                if product > palindrome or not palindrome:
                    palindrome = product
                    factors = [[i, j]]
                elif product == palindrome:
                    factors.append([i, j])
                j = 0
            j = j - 1
        i = i - 1
    return palindrome if palindrome else None, factors
