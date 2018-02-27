import math


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

    def position(self):
        return self.x, self.y

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

    def turn_to_turtle(self, turtle):
        t_x, t_y = turtle.position()
        if t_x > self.x and t_y > self.y:
            self.heading = math.degrees(math.sin(abs(self.y - t_y) / (math.sqrt((t_x - self.x) ** 2 + (t_y - self.y) ** 2))))
        elif t_x > self.x and t_y < self.y:
            self.heading = 360 - math.degrees(math.sin(abs(self.y - t_y) / (math.sqrt((t_x - self.x) ** 2 + (t_y - self.y) ** 2))))
        elif t_x < self.x and t_y > self.y:
            self.heading = 180 - math.degrees(math.sin(abs(self.y - t_y) / (math.sqrt((t_x - self.x) ** 2 + (t_y - self.y) ** 2))))
        elif t_x < self.x and t_y < self.y:
            self.heading = 180 + math.degrees(math.sin(abs(self.y - t_y) / (math.sqrt((t_x - self.x) ** 2 + (t_y - self.y) ** 2))))

    def connector(self, turtle):
        tx, ty = turtle.position()
        self.lines.append((self.x, self.y, tx, ty))

    def point(self):
        self.lines.append((self.x, self.y, self.x, self.y))

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
                file.write("<line x1=\"{}\" y1=\"{}\" x2=\"{}\" y2=\"{}\" style=\"stroke:black;stroke-width:1\" />\n".format(x1, y1, x2, y2))
            file.write("</svg>\n")