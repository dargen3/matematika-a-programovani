from matplotlib import pyplot as plt
from numba import jit


@jit(nopython=True)
def quadratic_distance(point_y, xm, k):
    return (point_y[1]-xm*point_y[0]-k)**2


@jit(nopython=True)
def find_parameters(points):
    final_xm = 1
    final_k = 0
    total_quadratic_distace = 0
    for distance in [quadratic_distance(point, final_xm, final_k) for point in points]:
        total_quadratic_distace += distance
    for xm in range(-40, 40):
        for k in range(-40, 40):
            actual_quadratic_distance = 0
            for distance in [quadratic_distance(point, xm, k) for point in points]:
                actual_quadratic_distance += distance
            if actual_quadratic_distance < total_quadratic_distace:
                total_quadratic_distace = actual_quadratic_distance
                final_k = k
                final_xm = xm
    return final_xm, final_k


def numerical_regression(file):
    points = []
    with open(file, "r") as data:
        for line in data.readlines():
            line = line.split()
            points.append((float(line[0]), float(line[1])))
    plt.plot([x[0] for x in points], [x[1] for x in points], "o", color="blue")
    plt.show()
    final_xm, final_k = find_parameters(points)
    print(final_xm, final_k)
    plt.plot([x[0] for x in points], [x[1] for x in points], "o", color="blue")
    plt.plot([0, 100], [final_xm*0 + final_k, final_xm*100 + final_k])
    plt.show()


def least_squares(file):
    points = []
    with open(file, "r") as data:
        for line in data.readlines():
            line = line.split()
            points.append((float(line[0]), float(line[1])))
    plt.plot([x[0] for x in points], [x[1] for x in points], "o", color="blue")
    plt.show()
    n = len(points)
    x = [points[x][0] for x in range(n)]
    y = [points[x][1] for x in range(n)]
    xm = (n * sum([x[a] * y[a] for a in range(n)]) - sum(x) * sum(y)) / (n * sum([x[a]**2 for a in range(n)]) - (sum(x))**2)
    k = (sum([x[a]**2 for a in range(n)]) * sum(y) - sum(x) * sum([x[a] * y[a] for a in range(n)])) / (n * sum([x[a]**2 for a in range(n)]) - (sum(x))**2)
    print(xm, k)
    plt.plot([x[0] for x in points], [x[1] for x in points], "o", color="blue")
    plt.plot([0, 100], [xm * 0 + k, xm * 100 + k])
    plt.show()

least_squares("linear.txt")

numerical_regression("linear.txt")
