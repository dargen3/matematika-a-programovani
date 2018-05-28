from random import randint
from pprint import pprint
from sys import exit

def create_maze(n):
    maze = [[randint(1,n-1) for x in range(n)] for x in range(n)]
    maze[n-1][n-1] = 0
    return maze


def solve_maze(maze):
    n = len(maze)
    # pprint(maze)
    visited = [((0, 0),(0, 0))]
    visited_points = [(0, 0)]
    last_len_visited = len(visited)
    to_jump = [(0, 0)]
    roads = []
    while True:
        points_to_delete = []
        points_new_jumps = []
        for point in to_jump:
            points_to_delete.append(point)
            x = point[0]
            y = point[1]
            value = maze[x][y]
            new_points = []
            if value != 0:
                for a in [-value, value]:
                    if n > x > -1 and n > y + a > -1:
                        new_points.append((x, y + a))
                    if n > x + a > -1 and n > y > -1:
                        new_points.append((x + a, y))
            for actual_point in new_points:
                actual_x = actual_point[0]
                actual_y = actual_point[1]
                if (actual_x, actual_y) in visited_points:
                    continue
                else:
                    if maze[actual_x][actual_y] != 0:
                        visited.append(((x, y),(actual_x, actual_y)))
                        visited_points.append((actual_x, actual_y))
                    if (actual_x, actual_y) not in points_new_jumps:
                        points_new_jumps.append((actual_x, actual_y))
                if maze[actual_x][actual_y] == 0:
                    p = ((x, y),(actual_x, actual_y))
                    road = [p]
                    while p[0] != (0, 0):
                        for a in visited:
                            if a[1] == p[0] and a not in road:
                                p = a
                                road.append(p)
                                continue
                    roads.append(road)
        for d in points_to_delete:
            to_jump.remove(d)
        for p in points_new_jumps:
            to_jump.append(p)
        if last_len_visited == len(visited):
            if len(roads) == 0:
                print("there is no solution")
            if len(roads) == 1:
                print("there is 1 solution")
                pprint(roads[0])
            if len(roads) > 1:
                print("there is {} solutions".format(len(roads)))
                distances = sorted([len(x) for x in roads])
                min_d = distances[0]
                unity = distances.count(min_d)
                pprint(roads)
                if unity == 1:
                    print("there is one shortest road")
                else:
                    print("there is {} shortest roads".format(unity))

            print("")
            exit()
        else:
            last_len_visited = len(visited)




solve_maze(create_maze(9))

