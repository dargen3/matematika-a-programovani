from combination import combinations
from permutation import permutation
from pprint import pprint


def variations(list_for_variations, k, repetition=False):
    per = []
    for c in combinations(list_for_variations, k, repetition):
        actual_permutations = permutation(c)
        if repetition:
            for x in actual_permutations:
                count = actual_permutations.count(x)
                if count > 1:
                    for y in range(count - 1):
                        actual_permutations.remove(x)
        per.extend(actual_permutations)
    return per

pprint(variations(["A", "B", "C", "D"], 2, repetition=True))
print("\n\n\n")
pprint(variations(["A", "B", "C", "D"], 2))
