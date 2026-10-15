# You are given an integer n. Your task is to find out the number of prime numbers in the range [1, n] (inclusive).
#  A prime number is defined as a number greater than 1 that has no divisors other than 1 and itself.
def countPrimes(n):
    count = 0
    for num in range(2,n+1):
        is_prime = True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            count += 1
    return count