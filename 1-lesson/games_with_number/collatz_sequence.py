def collatz_sequence(n):  # return number of steps of collatz sequence for n
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        count += 1
    return count

def largest_sequence(max):  # print number from interval (2, max) which have highest number of collatz steps
    num_of_steps = 0
    number = 0
    for x in range(2, max):
        count = collatz_sequence(x)
        if count > num_of_steps:
            num_of_steps = count
            number = x
    print(number)

largest_sequence(10000)
