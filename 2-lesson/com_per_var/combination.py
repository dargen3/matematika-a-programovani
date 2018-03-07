from pprint import pprint


def from_idx_to_var(list_to_comb, indexes):
    comb = []
    for x in indexes:
        comb.append(list_to_comb[x])
    return comb


def kernel(indexes, k, repetition, sum_of_items):
    if repetition:
        for x in range(1, k):
            if indexes[-x] < sum_of_items:
                indexes[-x - 1] += 1
                for y in range(x):
                    indexes[-x + y] = indexes[-x - 1]
                break
        return indexes
    else:
        for x in range(1, k):
            if indexes[-x] != indexes[-x - 1] + 1:
                indexes[-x - 1] += 1
                for y in range(x):
                    indexes[-x + y] = indexes[-x - 1] + y + 1
                break
        return indexes


def indx_cond(k, sum_of_items, repetition):
    if repetition:
        indexes = [0 for x in range(k)]
        condition = sum_of_items - 1
    else:
        indexes = [x for x in range(k)]
        condition = sum_of_items - k
    return indexes, condition


def combinations(list_for_combination, k, repetition=False):
    all_combinations = []
    sum_of_items = len(list_for_combination)
    indexes, condition = indx_cond(k, sum_of_items, repetition)
    all_combinations.append(from_idx_to_var(list_for_combination, indexes))
    while indexes[0] != condition:
        if indexes[-1] == sum_of_items - 1:
            indexes = kernel(indexes, k, repetition, sum_of_items)
            all_combinations.append(from_idx_to_var(list_for_combination, indexes))
        else:
            indexes[-1] += 1
            all_combinations.append(from_idx_to_var(list_for_combination, indexes))
    return all_combinations

if __name__ == '__main__':
    pprint(combinations(["a", "b", "c", "d"], 2))
    pprint("\n\n\n")
    pprint(combinations(["a", "b", "c", "d"], 2, repetition=True))

