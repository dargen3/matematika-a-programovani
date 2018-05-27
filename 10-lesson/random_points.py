from random import gauss, random


def make_clusters_points_file(file, poits):
    with open(file, "w") as file:
        for x, y, how_many, sigma in poits:
            for a in range(how_many):
                file.write("{} {}\n".format(gauss(x, sigma), gauss(y, sigma)))


def make_linear_points_file(file, points, xm, k, sigma):
    with open(file, "w") as file:
        for count in range(points):
            x = random() * 100
            y = xm * x + k
            file.write("{} {}\n".format(gauss(x, sigma), gauss(y, sigma)))


make_linear_points_file("linear.txt", 1000, 5, -20, 10)
make_clusters_points_file("clusters.txt", [[0, 0, 100, 1], [10, 10, 100, 1], [2, 10, 50, 1], [10, 0, 100, 2], [5, 5, 700, 0.5]])
