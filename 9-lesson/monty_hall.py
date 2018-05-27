from random import randint, choice


def game(mode):
    win = 0
    iteration = 100000
    for y in range(iteration):
        choices = [1, 2, 3]
        location = randint(1, 3)
        tip = randint(1, 3)
        hl = list(choices)
        hl.remove(location)
        try:
            hl.remove(tip)
            choices.remove(hl[0])
        except:
            choices.remove(choice(hl))
        if mode == "same":
            pass
        if mode == "random":
            tip = choice(choices)
        if mode == "change":
            choices.remove(tip)
            tip = choices[0]
        if tip == location:
            win += 1
    print(mode, "strategy result: {}".format(win/iteration*100))

game("same")
game("random")
game("change")
