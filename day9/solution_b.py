# Advent of Code 2023, Day 9, Solution B

import sys

from collections import defaultdict
from functools import reduce

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file days')

    filename = sys.argv[1]

    heightmap = []
    with open(filename) as file:
        for line in file.readlines():
            heightmap.append([int(c) for c in line.strip()])

    low_points = []
    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            p = (x, y)
            neighbors = get_neighbors(heightmap, p)
             
            if lower_than_neighbors(heightmap, p):
                low_points.append(p)

    basins = []
    seen = []

    for p in low_points:
        basin = []
        candidates = [p] 
        basins.append(basin)

        while candidates:
            candidate = candidates.pop()

            if candidate not in seen and in_basin(heightmap, candidate, basin):
                basin.append(candidate)
                seen.append(candidate)
                candidates.extend(get_neighbors(heightmap, candidate))

    dangers = sum(heightmap[p[0]][p[1]] + 1 for p in low_points)
    print('The danger is %s' % dangers)

    biggies = sorted([len(b) for b in basins], reverse=True)[0:3]
    print('The answer is %s' % (biggies[0] * biggies[1] * biggies[2]))


def is_lower(heightmap, a, b):
    return heightmap[a[0]][a[1]] < heightmap[b[0]][b[1]]


def is_higher(heightmap, a, b):
    return heightmap[a[0]][a[1]] > heightmap[b[0]][b[1]]


def in_basin(heightmap, p, basin):
    neighbors = get_neighbors(heightmap, p)
    height = heightmap[p[0]][p[1]]

    return height != 9 and (uphill_of_basin(heightmap, p, basin) or lower_than_neighbors(heightmap, p))


def lower_than_neighbors(heightmap, p):
    neighbors = get_neighbors(heightmap, p)
    return all(is_lower(heightmap, p, n) for n in neighbors)


def uphill_of_basin(heightmap, p, basin):
    neighbors = get_neighbors(heightmap, p)
    return any(is_higher(heightmap, p, n) and n in basin for n in neighbors)

def get_neighbors(heightmap, p):
    potential_neighbors = [(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)]
    return [n for n in potential_neighbors if in_bounds(heightmap, n)]


def in_bounds(heightmap, p):
    return p[0] >= 0 and p[1] >= 0 and p[0] < len(heightmap) and p[1] < len(heightmap[p[0]])


if __name__ == '__main__':
    run()
