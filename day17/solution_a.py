# Advent of Code 2021, Day 17, Solution A

import sys

from collections import namedtuple
from dataclasses import dataclass
from functools import reduce
from typing import Optional

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

    print('the answer is %i' %  ((abs(bounds.ly) * (abs(bounds.ly) - 1)) // 2))


if __name__ == '__main__':
    run()
