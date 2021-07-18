def is_armstrong_number(number: int) -> bool:
    num_str = str(number)
    num_len = len(num_str)
    num_sum = sum([(int(digit) ** num_len) for digit in num_str])
    return num_sum == number
