# Advent of Code 2023, Day 9, Solution A

import sys

from collections import defaultdict

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file days')

    filename = sys.argv[1]

    heightmap = []
    with open(filename) as file:
        for line in file.readlines():
            heightmap.append([int(c) for c in line.strip()])

    danger_zones = []
    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            point_height = heightmap[x][y]
            neighbors = [p for p in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if in_bounds(heightmap, p)]
             
            if all(point_height < heightmap[n[0]][n[1]] for n in neighbors):
                danger_zones.append((x, y))
    
    answer = sum([heightmap[p[0]][p[1]] + 1 for p in danger_zones])

    print('The answer is %i' % answer)


def in_bounds(heightmap, p):
    return p[0] >= 0 and p[1] >= 0 and p[0] < len(heightmap) and p[1] < len(heightmap[p[0]])


if __name__ == '__main__':
    run()
