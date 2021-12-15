# Advent of Code 2021, Day 15, Solution B

import math
import sys

from collections import defaultdict, namedtuple

Point = namedtuple('Point', ['x', 'y'])

def run():
    if len(sys.argv) < 3:
        raise ValueError('No arguments provided. Usage: solution.py replicas')

    filename = sys.argv[1]
    replicas = int(sys.argv[2])

    baseboard = []
    with open(filename) as file:
        # Normalize weights to 0 so that modulo math is easier later.
        baseboard = [[int(c) - 1 for c in line.strip()] for line in file.readlines()]
           
    board = baseboard * replicas
    for idx in range(len(board)):
        board[idx] = board[idx] * replicas

    for rx in range(replicas):
        for ry in range(replicas):
            for x in range(len(baseboard)):
                for y in range(len(baseboard[0])):
                    tx = x + (rx * len(baseboard))
                    ty = y + (ry * len(baseboard[0]))
                    board[tx][ty] = 1 + ((baseboard[x][y] + rx + ry) % 9)

    distances = defaultdict(lambda: sys.maxsize) 
    destination = Point(x=len(board)-1, y=len(board[0])-1)
    current = Point(x=0, y=0)
    distances[current] = 0
    potential_currents = set([current])

    visited = set()
    while current != destination:
        neighbors = get_unvisited_neighbors(current, board, visited)

        for n in neighbors:
            potential_currents.add(n)
            distance_to_neighbor = distances[current] + board[n.x][n.y] 
            if distance_to_neighbor < distances[n]:
                distances[n] = distance_to_neighbor

        visited.add(current)
        potential_currents.remove(current)
        current = get_next_current(potential_currents, visited, distances)

    print('The answer is %i' % distances[destination])


def get_next_current(potential_currents, visited, distances):
    distance = sys.maxsize
    point = None
    for p in potential_currents:
        if p not in visited and distances[p] < distance:
            distance = distances[p]
            point = p

    return point


def get_unvisited_neighbors(p, board, visited):
    neighbors = [Point(x=p.x+1, y=p.y), Point(x=p.x-1, y=p.y), Point(x=p.x, y=p.y-1), Point(x=p.x, y=p.y+1)]
    return [c for c in neighbors if in_bounds(c, board) and c not in visited]


def in_bounds(p, board):
    return p.x >= 0 and p.y >= 0 and p.x < len(board) and p.y < len(board[p.x])

if __name__ == '__main__':
    run()
