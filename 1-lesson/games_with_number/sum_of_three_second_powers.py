from math import sqrt


def is_sum_of_three(n):  # return boolean value, whether is n sum of three second powers
    sqrt_n = int(sqrt(n)) + 1
    for x in range(1, sqrt_n):
        for y in range(1, sqrt_n):
            for z in range(1, sqrt_n):
                if x**2 + y**2 + z**2 == n:
                    return True
    return False


def sum_of_false_number(max):  # print number of number which cannot be expressed like sum of three second powers from interval (1, max)
    false_number = 0
    for x in range(1, max+1):
        if not is_sum_of_three(x):
            false_number += 1
    print(false_number)

sum_of_false_number(1000)
