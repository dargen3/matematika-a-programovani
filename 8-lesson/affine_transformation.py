from math import cos, sin, radians
import sys
sys.path.insert(0, '/home/dargen3/python/matematika_a_programovani/1-lesson/graphic/')
from svg_turtle import SvgTurtle


class ATr:
    def __init__(self, points):
        self.input_points = points
        self.transformed_points = []
        self.all_homogenous_coordinates = []
        for x in self.input_points:
            self.all_homogenous_coordinates.append((x[0], x[1], 1))

    def _calculate(self):
        for index, point in enumerate(self.input_points):
            result = []
            for x in range(3):
                result.append(sum([self.matrix[x][y] * self.all_homogenous_coordinates[index][y] for y in range(3)]))
            self.transformed_points.append((result[0], result[1]))
        return self.transformed_points

    def translation(self, x_shift, y_shift):
        self.matrix = [[1, 0, x_shift], [0, 1, y_shift], [0, 0, 1]]
        return self._calculate()

    def scaling(self, x_scale, y_scale):
        self.matrix = [[x_scale, 0, 0], [0, y_scale, 0], [0, 0, 1]]
        return self._calculate()

    def rotation(self, angle):
        angle = radians(angle)
        self.matrix = [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]]
        return self._calculate()

    def own(self, a, b, c, d, e, f):
        self.matrix = [[a, b, e], [c, d, f], [0, 0, 1]]
        return self._calculate()


def affine_transformation(points, iteration=1, translation=False, rotation=False, scaling=False, write=False, own=False):
    set_of_points = [points]
    for x in range(iteration):
        transformed_points = set_of_points[-1]
        if translation:
            transformed_points = ATr(transformed_points).translation(translation[0], translation[1])
        if rotation:
            transformed_points = ATr(transformed_points).rotation(rotation)
        if scaling:
            transformed_points = ATr(transformed_points).scaling(scaling[0], scaling[1])
        if own:
            transformed_points = ATr(transformed_points).own(own[0], own[1], own[2], own[3], own[4], own[5])
        set_of_points.append(transformed_points)
    if write:
        x = 500
        y = 500
        turtle = SvgTurtle(x, y)
        for points in set_of_points:
            turtle.set_pos(points[0][0] + x, points[0][1] + y)
            for point in points + [points[0]]:
                turtle.set_pos(point[0] + x, point[1] + y, write=True)
        turtle.save("picture.svg")
    else:
        return transformed_points


points = [[0, 0], [0, 500], [500, 500], [500, 0]]
affine_transformation(points, iteration=50, rotation=20, scaling=(0.9, 0.9), translation=(5, 10), write=True)


def MRCM(points, transformations, iterations, name):
    points = [points]
    for x in range(iterations):
        new_points = []
        for point in points:
            for tr in transformations:
                new_points.append(affine_transformation(point, **tr))
        points = new_points
    set_of_points = points
    x = 500
    y = 500
    turtle = SvgTurtle(x, y)
    for points in set_of_points:
        turtle.set_pos(points[0][0] + x, points[0][1] + y)
        for point in points + [points[0]]:
            turtle.set_pos(point[0] + x, point[1] + y, write=True)
    turtle.save(name)


# MRCM(points, [{"own":[0.255, 0, 0, 0.255, 5*37.25, 5*67.14]}, {"own":[0.255, 0, 0, 0.255, 5*11.46, 5*22.32]}, {"own":[0.255, 0, 0, 0.255, 5*63.06, 5*22.32]}, {"own":[0.370, -0.642, 0.642, 0.370, 5*63.56, -0.61*5]}], 8, "star.svg")
# MRCM(points, [{"own":[0.849, 0.037, -0.037, 0.849, 5*7.5, 5*18.3]}, {"own":[0.197, -0.226, 0.226, 0.197, 5*40 , 5*4.9]}, {"own":[-0.15, 0.283, 0.26, 0.237, 5*57.5, 5*8.4]}, {"own":[0, 0, 0, 0.16, 5*50, 0*5]}], 8, "fern.svg")
# MRCM(points, [{"own":[0.5, 0, 0, 0.5, 5*50, 5*50]}, {"own":[0.5, 0, 0, 0.5, 500, 0]}, {"own":[0.5, 0, 0, 0.5, 0, 0]}], 8, "triangle.svg")
# MRCM(points, [{"own":[0, -0.5, 0.5, 0, 5*50, 5*50]}, {"own":[0.5, 0, 0, 0.5, 0, 0]}, {"own":[0.5, 0, 0, 0.5, 500, 0]}], 8, "triangle1.svg")
# MRCM(points, [{"own":[0.5, -0.5, 0.5, 0.5, 0, 0]}, {"own":[-0.5, -0.5, 0.5, -0.5, 500, 0]}], 13, "heighway.svg")
