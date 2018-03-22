from random import random
import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle
from math import sqrt
from operator import itemgetter


def is_there_intersection(ab, lines):
    if not len(lines):
        return False
    xa = ab[0]
    ya = ab[1]
    xb = ab[2]
    yb = ab[3]
    for line in lines:
        xc = line[0]
        yc = line[1]
        xd = line[2]
        yd = line[3]
        x = ((xa * yb - ya * xb) * (xc - xd) - (xa - xb) * (xc * yd - yc * xd)) / (
                    (xa - xb) * (yc - yd) - (ya - yb) * (xc - xd))
        y = ((xa * yb - ya * xb) * (yc - yd) - (ya - yb) * (xc * yd - yc * xd)) / (
                    (xa - xb) * (yc - yd) - (ya - yb) * (xc - xd))
        if round(y, 5) in [round(yb, 5), round(yb, 5), round(yc, 5), round(yd, 5)]:
            continue
        if min([xa, xb]) < x < max([xa, xb]) and min([xc, xd]) < x < max([xc, xd]) and min([ya, yb]) < y < max([ya, yb]) and min([yc, yd]) < y < max([yc, yd]):
            return True
    return False

def generate_points(n):
    points = []
    for point in range(n):
        x = random() * 1000
        y = random() * 1000
        points.append((x, y))
    return points

def calculate_length(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def triangulation(n):
    points = generate_points(n)
    lines = []
    for ia, a in enumerate(points):
        for ib, b in enumerate(points):
            if ib > ia:
                lines.append((a,b,calculate_length(a,b)))
    lines = sorted(lines, key=itemgetter(2))
    zofka = SvgTurtle(1000, 1000)
    printed_lines = []
    for line in lines:
        if not is_there_intersection((line[0][0], line[0][1], line[1][0], line[1][1]), printed_lines):
            zofka.line(line[0][0], line[0][1],line[1][0],line[1][1])
            printed_lines.append((line[0][0], line[0][1],line[1][0],line[1][1]))
    zofka.save("triangulation.svg")

triangulation(100)





