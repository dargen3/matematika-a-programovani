from random import random
import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle
from operator import itemgetter
from math import sqrt, acos, degrees, radians


def generate_points(n):
    points = []
    for point in range(n):
        x = random() * 1000
        y = random() * 1000
        points.append((x, y))
    return points


def calculate_length(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def is_convex(ab, lines):
    xa = ab[0]
    ya = ab[1]
    xb = ab[2]
    yb = ab[3]
    for line in lines:
        xc = line[0]
        yc = line[1]
        xd = line[2]
        yd = line[3]
        try:
            x = ((xa * yb - ya * xb) * (xc - xd) - (xa - xb) * (xc * yd - yc * xd)) / (
                        (xa - xb) * (yc - yd) - (ya - yb) * (xc - xd))
            y = ((xa * yb - ya * xb) * (yc - yd) - (ya - yb) * (xc * yd - yc * xd)) / (
                        (xa - xb) * (yc - yd) - (ya - yb) * (xc - xd))
            if round(y, 5) in [round(yb, 5), round(yb, 5), round(yc, 5), round(yd, 5)]:
                continue
            if min([xc, xd]) < x < max([xc, xd]) and min([yc, yd]) < y < max([yc, yd]):
                return False
        except ZeroDivisionError:
            pass
    return True


def convex_hull(points):
    points = sorted(points, key=itemgetter(0))
    angles = []
    for point in points[1:]:
        c = calculate_length(points[0], point)
        b = points[0][1] - point[1]
        angle = degrees(acos(b/c))
        angles.append(angle)
    points_angles = []
    for x in range(len(angles)):
        points_angles.append((points[x + 1], angles[x]))
    points_angles = [[points[0], 0]] + sorted(points_angles, key=itemgetter(1))
    points = [x[0] for x in points_angles]
    zofka = SvgTurtle(1000, 1000)
    for x, y in points:
        zofka.point(x, y)
    count = 1
    while count != 0:
        count = 0
        lines = [points[0] + points[1]]
        for x in range(1, len(points)):
            try:
                delete = True
                while delete:
                    if not is_convex(points[x] + points[x+1], lines):
                        print(x)
                        points.remove(points[x])
                        delete = True
                        count += 1
                    else:
                        delete = False
                        lines.append(points[x-1] + points[x])
            except IndexError:
                break
    for x in range(len(points)):
        zofka.line(points[x][0], points[x][1], points[x - 1][0], points[x - 1][1])
    zofka.save("convex_hull.svg")


convex_hull(generate_points(100))
