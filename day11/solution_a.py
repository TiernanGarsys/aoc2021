# Advent of Code 2021, Day 11, Solution A

import sys

from collections import namedtuple
from functools import reduce

Point = namedtuple('Point', ['x', 'y'])

def run():
    if len(sys.argv) < 3:
        raise ValueError('No arguments provided. Usage: solution.py input_file iterations')

    filename = sys.argv[1]
    iterations = int(sys.argv[2])
   
    board = [] 
    with open(filename) as file:
        for l in file.readlines():
            board.append([int(c) for c in l.strip()])

    answer = reduce(lambda a, n: a + iteration(board, n), range(iterations), 0)
    print('The answer is %i' % answer)


def iteration(board, n) -> int:
    """Returns the number of flashes that occurred on the current iteration"""

    increment(board, [Point(x=x, y=y) for x in range(len(board)) for y in range(len(board[x]))])

    flashes = 0
    active = True
    while active:
        active = False

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] >= 10:
                    board[x][y] = 0
                    flashes += 1
                    active = True

                    increment(board, get_flashed_neighbors(board, Point(x=x, y=y)))

    return flashes



def increment(board, target):
    for t in target:
        board[t.x][t.y] += 1


def get_flashed_neighbors(board, p):
    candidates = [Point(x=x, y=y) for x in range(p.x-1, p.x+2) for y in range(p.y-1, p.y+2)]
    return [c for c in candidates if in_bounds(board, c) and board[c.x][c.y] != 0 and c != p]


def in_bounds(board, p):
    return p.x >= 0 and p.y >= 0 and p.x < len(board) and p.y < len(board[p.x])


if __name__ == '__main__':
    run()
