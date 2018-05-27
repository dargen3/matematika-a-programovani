import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle

def n_square(n):
    zofka = SvgTurtle(500, 500)
    angle = (1 - 2 / n) * 180
    for x in range(n):
        zofka.forward(50)
        zofka.left(180 - angle)
    zofka.save("{}_square.svg".format(n))

def star(n):
    zofka = SvgTurtle(500, 500)
    for x in range(2*n):
        zofka.forward(150)
        zofka.left(180 - 180/n)
    zofka.save("star.svg")

n_square(7)
star(7)
