from random import choice, randint

def iters(mode):
    iter = 100000
    ka = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    kb = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6]
    both = [ka, kb]
    count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    if mode == "ka":
        for x in range(iter):
            count[choice(ka)] += 1
    if mode == "all_random":
        for x in range(iter):
            count[choice(both[randint(0,1)])] += 1
    if mode == "one_random":
        number = randint(0,1)
        for x in range(iter):
            count[choice(both[number])] += 1
    print(count)

iters("ka")
iters("all_random")
iters("one_random")