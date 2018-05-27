from math import factorial
from pprint import pprint


def replacing(some_list, x, y):
    helped_variable = some_list[x]
    some_list[x] = some_list[y]
    some_list[y] = helped_variable
    return some_list


def permutation(list_for_permutations):
    permutations = []
    sum_of_item = len(list_for_permutations)
    for period in range(factorial(sum_of_item - 1)):
        if period % 2 == 0:
            a = -1
            b = -1
            c = sum_of_item - 1
        else:
            a = 1
            b = 0
            c = 1
        for replace in range(sum_of_item-1):
            x = a * replace + b
            y = x + a
            list_for_permutations = replacing(list_for_permutations, x, y)
            permutations.append(list_for_permutations[:])
        x = c
        y = c - 1
        list_for_permutations = replacing(list_for_permutations, x, y)
        permutations.append(list_for_permutations[:])
    return permutations

if __name__ == '__main__':
    pprint(permutation([x for x in range(6)]))
