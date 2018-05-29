from pprint import pprint
import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle
from random import randint, choice


def in_walls(wall, walls):
    if wall in walls:
        return True
    if (wall[1], wall[0]) in walls:
        return True
    return False


def is_still_braid(walls, wall):
    aw = 0
    x1 = wall[0][0]
    y1 = wall[0][1]
    x2 = wall[1][0]
    y2 = wall[1][1]
    if x1 == x2:
        # under
        for wall in [((x1+1, y1), (x1+1, y2)), ((x1, y1), (x1+1, y1)), ((x2, y2), (x2+1, y2))]:
            if in_walls(wall, walls):
                aw += 1
        if aw > 1:
            return False
        else:
            aw = 0
        # above
        for wall in [((x1-1, y1), (x2-1, y2)), ((x1, y1), (x1-1, y1)), ((x2, y2), (x2-1, y2))]:
            if in_walls(wall, walls):
                aw += 1
        if aw > 1:
            return False
        return True
    else:
        # right
        for wall in [((x1, y1), (x1, y1+1)), ((x2, y2), (x2, y2+1)), ((x1, y1+1), (x2, y2+1))]:
            if in_walls(wall, walls):
                aw += 1
        if aw > 1:
            return False
        # left
        else:
            aw = 0
        for wall in [((x1, y1), (x1, y1-1)), ((x2, y2), (x2, y2-1)), ((x1, y1-1), (x2, y2-1))]:
            if in_walls(wall, walls):
                aw += 1
        if aw > 1:
            return False
    return True


def create_wall(x, y):
    r = randint(1, 4)
    if r == 1:
        wall = ((x, y), (x + 1, y))
    if r == 2:
        wall = ((x, y), (x - 1, y))
    if r == 3:
        wall = ((x, y), (x, y + 1))
    if r == 4:
        wall = ((x, y), (x, y - 1))
    return wall


def create_maze(n):
    walls = []
    points = []
    for x in range(1, n):
        for y in range(1, n):
            points.append((x, y))
    for x in range(n):
        walls.append(((0, x), (0, x+1)))
        walls.append(((x, n), (x+1, n)))
        walls.append(((n, x), (n, x+1)))
        walls.append(((x, 0), (x+1, 0)))
    while len(points):
        point = choice(points)
        x = point[0]
        y = point[1]
        c = 0
        while point in points:
            wall = create_wall(x, y)
            if in_walls(wall, walls):
                continue
            if is_still_braid(walls, wall):
                walls.append(wall)
                points.remove(point)
                try:
                    points.remove(wall[1])
                except:
                    pass
            c = c + 1
            if c > n*3:
                return False
    last_len = len(walls)
    while True:
        for x in range(n):
            for y in range(n):
                wall = create_wall(x, y)
                if in_walls(wall, walls):
                    continue
                if is_still_braid(walls, wall):
                    walls.append(wall)
        if last_len == len(walls):
            break
        last_len = len(walls)
    zofka = SvgTurtle(0, 0)
    for d in walls:
        zofka.line(d[0][0]*100, d[0][1]*100, d[1][0]*100, d[1][1]*100)
    zofka.save("p.svg")
    return True


def maze(n):
    r = False
    while r is not True:
        r = create_maze(n)

maze(10)
