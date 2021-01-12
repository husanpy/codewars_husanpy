def persistence(n):
    """takes in a positive parameter n and returns its multiplicative persistence,
       which is the number of times you must multiply the digits in num until 
       you reach a single digit"""
    count_frames = 1
    if n < 10:
        return 0
    multiplier = 1
    while n > 0:
        last_dig = n % 10
        multiplier *= last_dig
        n //= 10
    return count_frames + persistence(multiplier)
