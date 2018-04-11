import numpy as np
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


    def translation(self, x_shift, y_shift):
        for index, point in enumerate(self.input_points):
            matrix = [[1, 0, x_shift], [0, 1, y_shift], [0, 0, 1]]
            result = np.dot(matrix, self.all_homogenous_coordinates[index])
            self.transformed_points.append((result[0], result[1]))
        return self.transformed_points

    def scaling(self, x_scale, y_scale):
        for index, point in enumerate(self.input_points):
            matrix = [[x_scale, 0, 0], [0, y_scale, 0], [0, 0, 1]]
            result = np.dot(matrix, self.all_homogenous_coordinates[index])
            self.transformed_points.append((result[0], result[1]))
        return self.transformed_points

    def rotation(self, angle):
        angle = radians(angle)
        for index, point in enumerate(self.input_points):
            matrix = [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]]
            result = np.dot(matrix, self.all_homogenous_coordinates[index])
            self.transformed_points.append((result[0], result[1]))
        return self.transformed_points

    def own(self, a, b, c, d, e, f):
        for index, point in enumerate(self.input_points):
            matrix = [[a, b, e], [c, d, f], [0, 0, 1]]
            result = np.dot(matrix, self.all_homogenous_coordinates[index])
            self.transformed_points.append((result[0], result[1]))
        return self.transformed_points



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

#
points = [[0,0],[0,500],[500,500],[500,0]]
# affine_transformation(points, iterations=50, rotation=20, scaling=(0.9, 0.9), translation=(5, 10), write=True)



def MRCM(points, transformations, iterations, name):
    points = [points]
    for x in range(iterations):
        new_points = []
        for point in points:
            for tr in transformations:
                new_points.append(affine_transformation(point, **tr))
        points = new_points
    set_of_points = points

    # print(set_of_points)
    # from sys import exit
    # exit()
    x = 500
    y = 500
    turtle = SvgTurtle(x, y)

    for points in set_of_points:
        turtle.set_pos(points[0][0] + x, points[0][1] + y)
        for point in points + [points[0]]:
            turtle.set_pos(point[0] + x, point[1] + y, write=True)
    turtle.save(name)



MRCM(points, [{"own":[0.255, 0, 0, 0.255, 5*37.25, 5*67.14]}, {"own":[0.255, 0, 0, 0.255, 5*11.46, 5*22.32]}, {"own":[0.255, 0, 0, 0.255, 5*63.06, 5*22.32]}, {"own":[0.370, -0.642, 0.642, 0.370, 5*63.56, -0.61*5]}], 8, "star.svg")
# MRCM(points, [{"own":[0.255, 0, 0, 0.255, 0.3725, 0.6714]}, {"own":[0.255, 0, 0, 0.255, 0.1146, 0.2232]}, {"own":[0.255, 0, 0, 0.255, 0.6306, 0.2232]}, {"own":[0.370, -0.642, 0.642, 0.370, 0.6356, -0.0061]}], 3)






# MRCM(points, [{"scaling": (0.5, 0.5), "translation":(25, 0)}, {"scaling": (0.5, 0.5), "translation":(25, 0), "rotation":120},{"scaling": (0.5, 0.5), "translation":(25, 0), "rotation":-120}], 3)


