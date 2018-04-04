import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle
from random import choice, random
from math import sqrt


def n_square_points(n):
    zofka = SvgTurtle(550, 850)
    points = []
    angle = (1 - 2 / n) * 180
    for x in range(n):
        zofka.forward(400)
        zofka.left(180 - angle)
        points.append(list(zofka.position()))
    return points

def chaos_game(n, iterations, r, name, random=False):
    zofka = SvgTurtle(500, 800)
    points = n_square_points(n)
    if random:
        numbers = [x-100 for x in range(200)]
        for point in points:
            point[0] += choice(numbers)
            point[1] += choice(numbers)
    for point in range(len(points)):
        zofka.line(points[point][0], points[point][1], points[point-1][0], points[point-1][1])
    for x in range(iterations):
        point = choice(points)
        t = SvgTurtle(point[0], point[1])
        position = zofka.position()
        if position[0] > point[0]:
            posx = point[0] + abs(position[0] - point[0]) * r
        else:
            posx = position[0] + abs(position[0] - point[0]) * (1-r)
        if position[1] > point[1]:
            posy = point[1] + abs(position[1] - point[1]) * r
        else:
            posy = position[1] + abs(position[1] - point[1]) * (1-r)

        zofka.set_pos(posx, posy)
        zofka.self_point()
    zofka.save(name+".svg")



chaos_game(3, 10000, 0.5, "chaos_game")
chaos_game(3, 10000, 0.4, "chaos_game_0.4")
chaos_game(3, 10000, 0.6, "chaos_game_0.6")
chaos_game(3, 10000, 0.5, "chaos_game_random", random=True)
chaos_game(5, 10000, 0.4, "chaos_game_random_5_0.4", random=True)

