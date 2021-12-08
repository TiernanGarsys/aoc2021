# Advent of Code 2023, Day 7, Solution A

import functools
import sys


def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file days')

    filename = sys.argv[1]

    positions = []
    with open(filename) as f:
        positions = [int(p) for p in f.read().split(',')] 

    def cost_fxn(p1, p2):
        distance = abs(p1 - p2)
        return (distance * (distance + 1)) / 2

    pos_range = range(min(positions), max(positions) + 1)
    costs = [functools.reduce(lambda a, p: a + cost_fxn(pos, p), positions, 0) for pos in pos_range]
    print('The answer is %i' % min(costs))

if __name__ == '__main__':
    run()
