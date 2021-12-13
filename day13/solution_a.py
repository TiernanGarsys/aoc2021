# Advent of Code 2021, Day 12, Solution A

import sys

from collections import defaultdict, namedtuple
from enum import Enum
from functools import reduce

class Axis(Enum):
    VERTICAL = 'x'
    HORIZONTAL = 'y'

Fold = namedtuple('Fold', ['axis', 'position'])
Point = namedtuple('Point', ['x', 'y'])

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file {folds}')

    filename = sys.argv[1]
    folds_arg = int(sys.argv[2]) if len(sys.argv) >= 3 else 0

    points = set()
    folds = []
    with open(filename) as file:
        for line in file.readlines():
            if ',' in line:
                tokens = line.split(',')
                points.add(Point(x=int(tokens[0].strip()), y=int(tokens[1].strip())))
            elif '=' in line:
                tokens = line.split()[-1].split('=')
                folds.append(Fold(axis=Axis(tokens[0].strip()), position=int(tokens[1].strip())))
            else:
                continue

    folds = folds[:folds_arg] if folds_arg else folds
    
    for f in folds:
        folded_points = set()
        for p in points:
            if f.axis == Axis.VERTICAL and p.x > f.position:
                folded_points.add(Point(x=f.position - (p.x - f.position), y=p.y))
            elif f.axis == Axis.HORIZONTAL and p.y > f.position:
                folded_points.add(Point(x=p.x, y=f.position - (p.y - f.position)))
            else:
                folded_points.add(p)

        points = folded_points

    print('The answer is %i' % len(points))



if __name__ == '__main__':
    run()
