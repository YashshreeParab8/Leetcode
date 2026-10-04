def check_perfect_number(num):
    if num <= 1:
        return False
    
    total = 1  # 1 is always a divisor (except for num=1, handled above)
    i = 2
    while i * i <= num:
        if num % i == 0:
            total += i
            if i != num // i:  # avoid double-counting the square root
                total += num // i
        i += 1
    
    return total == num