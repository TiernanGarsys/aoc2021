# Advent of Code 2021, Day 2

import sys

from enum import Enum
from functools import reduce
from typing import NamedTuple


class Direction(Enum):
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'


class State(NamedTuple):
    horizontal: int = 0
    depth: int = 0
    aim: int = 0


class Delta(NamedTuple):
    direction: Direction
    magnitude: int


def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file')

    filename = sys.argv[1]
   
    deltas = []
    with open(filename) as file:
        deltas = [parse_delta(line) for line in file.readlines()]

    final_position = reduce(get_final_position, deltas, State(0, 0))
    product = final_position.horizontal * final_position.depth

    print('The final position is %s' % str(final_position))
    print('The product is %i' % product)


def parse_delta(raw: str) -> Delta:
    tokens = raw.strip().split()
    return Delta(direction=Direction(tokens[0]), magnitude=int(tokens[1]))


def get_final_position(start: State, delta: Delta) -> State:
    if delta.direction == Direction.FORWARD:
        return State(horizontal=start.horizontal + delta.magnitude, 
                     depth=start.depth + (delta.magnitude * start.aim), 
                     aim=start.aim)
    elif delta.direction == Direction.DOWN:
        return State(horizontal=start.horizontal, 
                     depth=start.depth,
                     aim=start.aim + delta.magnitude)
    elif delta.direction == Direction.UP:
        return State(horizontal=start.horizontal, 
                     depth=start.depth,
                     aim=start.aim - delta.magnitude)
    else:
        raise ValueError('Invalid direction for input delta: %s' % repr(delta))


if __name__ == '__main__':
    run()
