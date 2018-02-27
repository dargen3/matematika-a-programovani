from math import sqrt

def is_prime(potencial_prime):  # return boolean value, whether number is prime number
    if potencial_prime == 1:
        return False
    elif potencial_prime == 2:
        return True
    elif potencial_prime %2 == 0:
        return False
    for x in range(3, int(sqrt(potencial_prime))+1, 2):
        if potencial_prime % x == 0:
            return False
    return True

def sum_of_prime_withou_three(max):  # print sum of all prime numbers in interval (1, max) which not contain 3
    sum_of_primes = 0
    for x in range(1, max + 1):
        if is_prime(x):
            if "3" not in str(x):
                sum_of_primes += x
    print(sum_of_primes)

sum_of_prime_withou_three(1000)