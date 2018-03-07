import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle


def sierpinski_triangle(depth, base, zofka):
    if depth == 0:
        for x in range(3):
            zofka.forward(base)
            zofka.left(120)
    else:
        for x in range(3):
            sierpinski_triangle(depth-1, base, zofka)
            zofka.forward(base*2**depth, write=False)
            zofka.left(120)
    zofka.save("sierpinski_triangle.svg")



zofka = SvgTurtle(1000, 1000)
sierpinski_triangle(6, 15, zofka)