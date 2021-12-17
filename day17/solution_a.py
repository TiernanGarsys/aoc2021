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
  
    # We know the probe will always pass downward through the x-axis at negative initial y velocity. 
    # Assuming this, the best case is that it will, on the next step after passing through the x-axis, 
    # be in the target area at the bottom-most point; if it were launched any higher and thus moving
    # any faster, it would surpass the target zone in a single step. Thus, the highest magnitude
    # velocity at this point that can still hit the target zone is -bounds.ly. 
    # 
    # Because the probe velocity decreases by 1 each step, the optimal Y velocity is -bounds.ly, 
    # and the Y velocity is 0 at the peak, we can infer that the maximum height is the sum
    # of all integers from 0 to abs(bounds.ly).
    print('the answer is %i' %  ((abs(bounds.ly) * (abs(bounds.ly) - 1)) // 2))


if __name__ == '__main__':
    run()
