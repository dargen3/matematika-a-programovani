import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle


def sierpinski_penta(depth, base, zofka):
    if depth == 0:
        for i in range(5):
            zofka.forward(base)
            zofka.left(72)
    else:
        for x in range(5):
            sierpinski_penta(depth-1, base, zofka)
            zofka.forward(base*2.62**depth, write=False)
            zofka.left(72)
        for x in range(2):
            zofka.forward(base*2.62**(depth-1))
            zofka.left(72)
        zofka.right(108)
        sierpinski_penta(depth-1, base, zofka)
        zofka.right(144)
        for x in range(2):
            zofka.forward(base*2.62**(depth-1))
            zofka.right(72)
        zofka.left(180+72)
    zofka.save("sierpinski_penta.svg")

zofka = SvgTurtle(1000, 1000)
sierpinski_penta(4, 10, zofka)
