from random import random
from math import sin, cos, radians, degrees


def generate_line(n, length, scope):
    lines = []
    for a in range(n):
        x1 = random() * scope * 2 - scope
        y1 = random() * scope * 2 - scope
        angle = random() * 360
        x2 = cos(radians(angle)) * length + x1
        y2 = sin(radians(angle)) * length + y1
        lines.append((x1, y1, x2, y2))
    return lines


def find_intersections(lines):
    for indexab, ab in enumerate(lines):
        for indexcd, cd in enumerate(lines):
            if indexcd > indexab:
                xa = ab[0]
                ya = ab[1]
                xb = ab[2]
                yb = ab[3]
                xc = cd[0]
                yc = cd[1]
                xd = cd[2]
                yd = cd[3]
                x = ((xa * yb - ya * xb) * (xc - xd) - (xa - xb) * (xc * yd - yc * xd)) / ((xa - xb) * (yc - yd) - (ya - yb) * (xc - xd))
                y = ((xa * yb - ya * xb) * (yc - yd) - (ya - yb) * (xc * yd - yc * xd)) / ((xa - xb) * (yc - yd) - (ya - yb) * (xc - xd))
                if round(y, 5) in [round(yb, 5), round(yb, 5), round(yc, 5), round(yd, 5)]:
                    continue
                if min([xa, xb]) < x < max([xa, xb]) and min([xc, xd]) < x < max([xc, xd]) and min([ya, yb]) < y < max(
                        [ya, yb]) and min([yc, yd]) < y < max([yc, yd]):
                    print(x, y)

find_intersections(generate_line(100, 10, 20))
