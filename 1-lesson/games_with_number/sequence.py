def NSD(a, b):  # return NSD according to euklid's algorythm
    if b < a:
        a, b = b, a
    while b != 0:
        modulo = a % b
        a = b
        b = modulo
    return a


def sequence(max):  # return first number of sequence, which are higher then max
    sequence = [1, 1]  # first and second item of sequence are 1, 1. all another number is addition of two previous number and their NSD
    while sequence[-1] < max:
        sequence.append(sequence[-1] + sequence[-2] + NSD(sequence[-1], sequence[-2]))
    print(sequence[-1])

sequence(1000000)
