import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle


def feigenbaum():
    y_range = input("Zadej y rozsah oddelene - od nuly do 1. Napriklad 0.25-0.75: ").split("-")
    x_range = input("Zadej x rozsah oddelene - od nuly do 1. Napriklad 0.25-0.75: ").split("-")
    y_range[0] = float(y_range[0])
    y_range[1] = float(y_range[1])
    x_range[0] = float(x_range[0])
    x_range[1] = float(x_range[1])
    points = int(200 * abs(1/abs(y_range[0]-y_range[1])))
    start = 0.5
    min = 2
    max = 4
    y = start
    diference = int(200 * abs(1/abs(y_range[0]-y_range[1])))
    zofka = SvgTurtle(0, 0)
    for x in range(min*diference, max*diference):
        x = x/diference
        for point in range(points):
            y = x * y * (1.0 - y)
            if y_range[0] < y < y_range[1] and x_range[0] < (x-2)/2 < x_range[1]:
                zofka.set_pos(((x-2)*500-x_range[0]*1000)*(1/abs(x_range[0]-x_range[1])),
                              (y*1000-y_range[0]*1000)*(1/abs(y_range[0]-y_range[1])))
                zofka.self_point()
    zofka.save("feigenbaum.svg")

feigenbaum()
