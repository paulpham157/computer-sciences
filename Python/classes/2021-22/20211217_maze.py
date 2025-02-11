# Copyright © 2021 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.

from pprint import pprint

FILE_NAME = '20211217_maze.txt'
MAZE_WALL = '*'
MAZE_CORRIDOR = ' '


def read_maze(filename):
    maze = list()
    with open(filename) as input_file:
        for line in input_file:
            maze.append(list(line[:-1]))
    return maze


def is_corridor(maze, row, column):
    if row < 0 or row >= len(maze):
        return False
    elif column < 0 or column >= len(maze[row]):
        return False
    elif maze[row][column] == MAZE_WALL:
        return False
    elif maze[row][column] == MAZE_CORRIDOR:
        return True


def main():
    maze = read_maze(FILE_NAME)
    pprint(maze)
    corridors = dict()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if is_corridor(maze, row, column):
                corridors[(row, column)] = set()
                for r, c in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
                    if is_corridor(maze, row + r, column + c):
                        corridors[(row, column)].add((row + r, column + c))
    pprint(corridors)


if __name__ == '__main__':
    main()
