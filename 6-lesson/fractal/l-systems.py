from turtle import Turtle
from random import randint


fractals = {
    "kv": {
        "start": "F--F--F",
        "predpisy": {"F": "F+F--F+F"},
        "rules": {"F": "forward_10", "+": "turn_60", "-": "turn_-60"},
        "iters": 4},
    "st": {
        "start": "A",
        "predpisy": {"A": "B-A-B", "B": "A+B+A"},
        "rules": {"A": "forward_5", "B": "forward_5", "+": "turn_60", "-": "turn_-60"},
        "iters": 6},
    "hk": {
        "start": "A",
        "predpisy": {"A": "-BF+AFA+FB-", "B": "+AF-BFB-FA+"},
        "rules": {"F": "forward_5", "+": "turn_91", "-": "turn_-90"},
        "iters": 5},
    "strom": {
        "start": "A",
        "predpisy": {"A": "F[+A]-A", "F": "FF"},
        "rules": {"A": "forward_5", "F": "forward_5", "+": "turn_45", "-": "turn_-45"},
        "iters": 7},
    "stf": {
        "start": "F-G-G",
        "predpisy": {"G": "GG", "F": "F-G+F+G-F"},
        "rules": {"G": "forward_5", "F": "forward_5", "+": "turn_120", "-": "turn_-120"},
        "iters": 4},
    "plant": {
        "start": "X",
        "predpisy": {"F": "FF", "X": "F+[[X]-X]-F[-FX]+X"},
        "rules": {"F": "forward_5", "+": "turn_25", "-": "turn_-25"},
        "iters": 5},
    "plant_stochastic": {
        "start": "F",
        "predpisy": ["F", "F[+F]F[-F]F", "F[+F]F", "F[-F]F"],
        "rules": {"F": "forward_5", "+": "turn_30", "-": "turn_-30"},
        "iters": 5}
}


def l_system(name):
    fractal = fractals[name]
    final_string = fractal["start"]
    rules = fractal["rules"]
    predpisy = fractal["predpisy"]
    zofka = Turtle()
    zofka.speed(0)
    if type(predpisy) == dict:
        for x in range(fractal["iters"]):
            actual_string = ""
            for y in final_string:
                if y in predpisy:
                    actual_string += predpisy[y]
                else:
                    actual_string += y
            final_string = actual_string
    elif type(predpisy) == list:
        for x in range(fractal["iters"]):
            actual_string = ""
            for y in final_string:
                if y in predpisy[0]:
                    actual_string += predpisy[randint(1, len(predpisy)-1)]
                else:
                    actual_string += y
            final_string = actual_string
    zasobnik = []
    for x in final_string:
        if x == "[":
            zasobnik.append((zofka.pos(), zofka.heading()))
        elif x == "]":
            position = zasobnik.pop(-1)
            zofka.penup()
            zofka.setpos(position[0][0], position[0][1])
            zofka.pendown()
            zofka.setheading(position[1])
        try:
            do = rules[x].split("_")
            if do[0] == "forward":
                zofka.forward(int(do[1]))
            elif do[0] == "turn":
                zofka.right(int(do[1]))
        except KeyError:
            pass


l_system("plant_stochastic")
