from random import choice
from pprint import pprint


def print_maze(maze):
    print(" ", end="")
    for x in range(7):
        print("_", end="")
    print("_")
    for x in range(6):
        print("|", end="")
        for y in range(7):
            print(maze[x][y], end="")
        print("|")
    print(" ", end="")
    for x in range(7):
        print("¯", end="")
    print()
    return(maze)

maze = [
    ["A"," "," "," "," "," "," "],
    [" "," ","#","#","#","#"," "],
    ["#"," "," ","#","#","#"," "],
    ["#","#"," "," ","#","#"," "],
    ["#","#","#"," "," ","#"," "],
    ["#","#","#","#"," ","B"," "],
    ]



def count_action(road):
    len(road)
    count = 0
    if road[0][0][0] == road[0][1][0]:
        start = 1
    else:
        start = 0
    for x in road[1:]:
        if x[0][0] == x[1][0]:
            s = 1
        else:
            s = 0

        if s != start:
            count += 1
            start = s
    return count + len(road)



def solve(maze):
    print_maze(maze)
    xn = len(maze)
    yn = len(maze[0])
    for a in range(xn):
        for b in range(yn):
            if maze[a][b] == "A":
                visited = [((a, b),(a, b))]
    last_len_visited = len(visited)
    to_jump = [visited[0][0]]
    roads = []
    while True:
        points_to_delete = []
        points_new_jumps = []
        for point in to_jump:
            points_to_delete.append(point)
            x = point[0]
            y = point[1]
            new_points = []
            if maze[x][y] != "B":
                for a in [-1, +1]:
                    if xn > x > -1 and yn > y + a > -1:
                        new_points.append((x, y + a))
                    if xn > x + a > -1 and yn > y > -1:
                        new_points.append((x + a, y))
            for actual_point in new_points:
                actual_x = actual_point[0]
                actual_y = actual_point[1]
                if (actual_x, actual_y) in [x[1] for x in visited]:
                    continue
                if maze[actual_x][actual_y] == "#":
                    continue
                else:
                    if maze[actual_x][actual_y] != "B":
                        visited.append(((x, y),(actual_x, actual_y)))
                    if (actual_x, actual_y) not in points_new_jumps:
                        points_new_jumps.append((actual_x, actual_y))
                if maze[actual_x][actual_y] == "B":
                    p = ((x, y),(actual_x, actual_y))
                    road = [p]
                    while p[0] != visited[0][0]:
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
            else:
                actions = []
                for road in roads:
                    actions.append(count_action(road))
                best_road = roads[actions.index(min(actions))]
                pprint(best_road)
                for point in best_road[:-1]:
                    maze[point[0][0]][point[0][1]] = "."
                print_maze(maze)
                print("Actions: {}".format(min(actions)))
            print("")
            exit()
        else:
            last_len_visited = len(visited)




solve(maze)
