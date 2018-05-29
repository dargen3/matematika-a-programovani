import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle


def my_picture():
    zofka = SvgTurtle(500, 500)
    angle = 1
    for x in range(10000):
        zofka.forward(40)
        zofka.left(angle)
        angle += 5
        if x % 3 == 0:
            angle -= 5
    zofka.save("my_awsome_svg.svg")

my_picture()