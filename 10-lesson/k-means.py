from matplotlib import pyplot as plt
from random import choice
from math import sqrt


def k_means(file, clusters, iters):
    points = []
    colors = ["red", "blue", "green", "black", "yellow"]
    with open(file, "r") as data:
        for line in data.readlines():
            line = line.split()
            points.append((float(line[0]), float(line[1])))
    means = []
    while len(means) != clusters:
        mean = choice(points)
        if mean not in means:
            means.append(mean)
    plt.plot([x[0] for x in points], [x[1] for x in points], "o", color="blue")
    plt.show()

    points_near_mean = [[] for x in range(clusters)]
    for x in range(iters):
        for point in points:
            distances = []
            for mean in means:
                distances.append(sqrt((mean[0] - point[0])**2 + (mean[1] - point[1])**2))
            points_near_mean[distances.index(min(distances))].append(point)
        for y in range(clusters):
            means[y] = (sum([x[0] for x in points_near_mean[y]])/len(points_near_mean[y]), sum([x[1] for x in points_near_mean[y]])/len(points_near_mean[y]))
    for index, p_set in enumerate(points_near_mean):
        plt.plot([x[0] for x in p_set], [x[1] for x in p_set], "o", color=colors[index])
    plt.show()


k_means("clusters.txt", 5, 50)
