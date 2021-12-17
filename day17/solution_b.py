# Advent of Code 2021, Day 17, Solution B

import sys

from collections import namedtuple

Bounds = namedtuple('Bounds', ['lx', 'hx', 'ly', 'hy'])

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file ')

    filename = sys.argv[1]
    bounds = None
    with open(filename) as file:
        tokens = file.read().split()
        xb = tokens[2][2:-1].split('..')
        yb = tokens[3][2:].split('..')
        bounds = Bounds(lx=int(xb[0]), hx=int(xb[1]), ly=int(yb[0]), hy=int(yb[1]))

    total = 0
    for ivx in range(0, max(bounds.hx, 0) + 1):
        for ivy in range(bounds.ly, abs(bounds.hy) * 2 + 1):
            total += simulate(ivx, ivy, bounds)

    print('The answer is %i' % total)

def simulate(vx, vy, bounds):
    x = y = 0
    while underbounds(x, y, bounds):
        if in_bounds(x, y, bounds):
            return 1
        x += vx
        y += vy
        if vx < 0:
            vx += 1
        elif vx > 0:
            vx -= 1
        vy -= 1
    return 0


def underbounds(x, y, bounds):
    return abs(x) <= max(abs(bounds.lx), abs(bounds.hx)) and y >= bounds.ly


def in_bounds(x, y, bounds):
    return bounds.lx <= x <= bounds.hx and bounds.ly <= y <= bounds.hy

if __name__ == '__main__':
    run()
