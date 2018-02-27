def all_divisors(n):  # return number of all divisors for n
    divisors = 0
    for x in range(1, n + 1):
        if n % x == 0:
            divisors += 1
    return divisors

def num_with_most_divisors(max):  # return list of pairs [(number, number of divisors),...] with numbers with highest number of divisors from interval (2, max)
    num_and_divisors = [(0, 0)]
    for x in range(1, max):
        count = all_divisors(x)
        if count > num_and_divisors[-1][1]:
            num_and_divisors = [(x, count)]
        elif count == num_and_divisors[-1][1]:
            num_and_divisors.append((x, count))
        else:
            continue
    for x in num_and_divisors:
        print(x[0])

num_with_most_divisors(10000)