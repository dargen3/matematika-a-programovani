from math import sqrt, asin, degrees, sin, radians
import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle


def squares():
    zofka = SvgTurtle(500, 500)
    length = 400
    cor_length = sqrt(0.75**2 + 0.25**2)
    cor_angle = degrees(asin(0.25/cor_length))
    for y in range(50):
        for x in range(4):
            zofka.forward(length)
            zofka.right(90)
        zofka.forward(length*0.25)
        zofka.right(cor_angle)
        length = length * cor_length
    zofka.save("squares_in_squares.svg")

# squares()


def n_square(zofka, n):
    angle = (1 - 2 / n) * 180
    for x in range(n):
        zofka.forward(50)
        zofka.left(180 - angle)


def blow():
    zofka = SvgTurtle(500, 500)
    for x in range(12):
        zofka.left(360/12)
        n_square(zofka, 12)
    zofka.save("blow.svg")


# blow()

def ring_with_lines():
    zofka = SvgTurtle(500, 500)
    for x in range(-200, 201, 25):
        value = sqrt(200**2 - x**2)
        y = x + 500
        zofka.line(y, 500 + value, y, 500 - value)
        zofka.line(500 + value, y, 500 - value, y)
    zofka.save("ring_lines.svg")

# ring_with_lines()


def triangles():
    zofka = SvgTurtle(500, 500)
    length = 30
    zofka.left(90)
    for x in range(15):
        positions = []
        for x in range(3):
            zofka.forward(length, write=False)
            positions.append(zofka.position())
            zofka.left(180)
            zofka.forward(length, write=False)
            zofka.right(60)
        positions.append(positions[0])
        for x in range(3):
            zofka.line(positions[x][0], positions[x][1], positions[x+1][0], positions[x+1][1])
        length += 30
    zofka.save("triangles.svg")

# triangles()


def pentagram_relative():
    zofka = SvgTurtle(500, 500)
    for x in range(5):
        zofka.forward(200)
        zofka.left(180 - 36)
    zofka.right(36)
    length = 100/sin(radians(54))
    angle = (1 - 2 / 5) * 180
    for x in range(5):
        zofka.forward(length)
        zofka.left(180 - angle)
    zofka.save("relative_pentagram.svg")

# pentagram_relative()


def pentagram_absolute():
    zofka = SvgTurtle(500, 500)
    angle = (1 - 2 / 5) * 180
    positions = []
    for x in range(5):
        zofka.forward(200)
        zofka.left(180-108)
        positions.append(zofka.position())
    for x in range(5):
        zofka.line(positions[x][0], positions[x][1], positions[x-1][0], positions[x-1][1])
    for x in range(5):
        zofka.line(positions[x][0], positions[x][1], positions[x - 2][0], positions[x - 2][1])
    zofka.save("absolute_pentragram.svg")

pentagram_absolute()
