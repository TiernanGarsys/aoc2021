# Advent of Code 2021, Day 15, Solution A

import sys

from collections import defaultdict, namedtuple

Point = namedtuple('Point', ['x', 'y'])

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file ')

    filename = sys.argv[1]

    board = []
    with open(filename) as file:
        board = [[int(c) for c in line.strip()] for line in file.readlines()]
    
    visited = []
    distances = defaultdict(lambda: sys.maxsize) 
    destination = Point(x=len(board)-1, y=len(board[0])-1)
    current = Point(x=0, y=0)
    distances[current] = 0
    potential_currents = set([current])

    while current:
        neighbors = get_unvisited_neighbors(current, board, visited)

        for n in neighbors:
            potential_currents.add(n)
            distance_to_neighbor = distances[current] + board[n.x][n.y] 
            if distance_to_neighbor < distances[n]:
                distances[n] = distance_to_neighbor

        visited.append(current)
        potential_currents.remove(current)

        if current == destination:
            break

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
