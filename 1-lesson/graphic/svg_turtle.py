import math
from math import acos, degrees

class SvgTurtle:
    """
    SvgTrutle is modul, which has similar behavior like normal turtle graphic in python2/3.
    Module is still in develop.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heading = 0.0
        self.lines = []
        self.points = []

    def position(self):
        return self.x, self.y

    def line(self, x1, y1, x2, y2):
        self.lines.append((x1, y1, x2, y2))

    def left(self, angle):
        self.heading -= angle

    def right(self, angle):
        self.heading += angle

    def forward(self, distance, write=True, back=False):
        nx = self.x + distance * math.cos(self.heading * math.pi / 180)
        ny = self.y + distance * math.sin(self.heading * math.pi / 180)
        if write:
            self.lines.append((self.x, self.y, nx, ny))
        if not back:
            self.x, self.y = nx, ny


    def connector(self, turtle):
        tx, ty = turtle.position()
        self.lines.append((self.x, self.y, tx, ty))


    def point(self, x, y):
        self.points.append((x, y))

    def self_point(self):
        self.points.append((self.x, self.y))

    def set_angle(self, angle):
        self.heading = angle

    def set_pos(self, x, y, write=False, back=False):
        if write:
            self.lines.append((self.x, self.y, x, y))
        if not back:
            self.x, self.y = x, y
            self.heading = 0

    def save(self, filename):
        with open(filename, "w") as file:
            file.write("<svg>\n")
            for x1, y1, x2, y2 in self.lines:
                file.write("<line x1=\"{}\" y1=\"{}\" x2=\"{}\" y2=\"{}\" style=\"stroke:black;stroke-width:3\" />\n".format(x1, y1, x2, y2))
            for x, y in self.points:
                file.write("<circle cx=\"{}\" cy=\"{}\" r=\"1\" stroke=\"black\" stroke-width=\"1\" fill=\"red\" />".format(x,y))
            file.write("</svg>\n")