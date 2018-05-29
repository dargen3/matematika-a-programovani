from svg_turtle import SvgTurtle
from math import sin, pi
from time import sleep


def svg_star(lines, tops, radius, name):  # save svg file with star
    turtle = SvgTurtle(400, 400)
    angle = 180 - (1 - (2 / (lines * tops))) * 180
    distance = radius * 2 * sin(pi / (lines * tops))  # needed calculations for star
    for top in range(tops):
        for x in [-1, 1]:
            turtle.set_pos(400, 400)
            turtle.left(360/tops * top)
            turtle.forward(radius)
            turtle.left(x * 180 - x * angle/2)
            end_of_line = SvgTurtle(400, 400)
            end_of_line.right(360 / tops * (x - top))
            for line in range(lines):
                turtle.left(x * angle)
                turtle.forward(distance)
                end_of_line.forward(radius/lines)
                turtle.connector(end_of_line)
    turtle.save(name)

svg_star(20, 4, 400, "star.svg")
svg_star(20, 5, 400, "star5.svg")
svg_star(20, 6, 400, "star6.svg")
svg_star(20, 10, 400, "star10.svg")
