from random import randint, choice


def bayes(cubes, attempts):
    f = 0
    n = 0
    normal_cube = [1, 2, 3, 4, 5, 6]
    false_cube = [6, 6, 6, 6, 6, 6]
    for y in range(100000):
        numbers = []
        cube = randint(1, cubes)
        if cube == 1:
            cube = false_cube
            mode = "false"
        else:
            cube = normal_cube
            mode = "normal"
        for x in range(attempts):
            numbers.append(choice(cube))
        if sum(numbers) == attempts*6:
            if mode == "normal":
                n += 1
            else:
                f += 1
    print(n/(n+f))
bayes(100, 3)
