# Advent of Code 2021, Day 5, Solution B

import sys

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum, auto


class Orientation(Enum):
    VERTICAL = auto()
    HORIZONTAL = auto()
    DIAGONAL = auto()


@dataclass
class Point():
    x: int
    y: int


@dataclass
class Line():
    start: Point
    end: Point
    orientation: Orientation


def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file')

    filename = sys.argv[1]
   
    lines = []
    with open(filename) as file:
        for raw_line in file.readlines():
            line = parse_line(raw_line)
            if line:
                lines.append(line)


    board = populate_board(lines)
    intersections = 0

    for row in board.values():
        for pos in row.values():
            if pos > 1:
                intersections += 1

    print('The answer is %i' % intersections)


def parse_line(r: str) -> Line:
    tokens = r.strip().split()

    start_tokens = tokens[0].split(',')
    end_tokens = tokens[2].split(',')

    start = Point(x=int(start_tokens[0]), y=int(start_tokens[1]))
    end = Point(x=int(end_tokens[0]), y=int(end_tokens[1]))

    orientation = None
    if (start.x != end.x) and (start.y != end.y):
        orientation = Orientation.DIAGONAL
    elif start.x == end.x:
        orientation = Orientation.VERTICAL
    else:
        orientation = Orientation.HORIZONTAL

    return Line(start=start, end=end, orientation=orientation)


def populate_board(lines):
    board = defaultdict(lambda: defaultdict(int))

    for line in lines:
        if line.orientation == Orientation.HORIZONTAL:
            y = line.start.y
            min_x = min(line.start.x, line.end.x)
            max_x = max(line.start.x, line.end.x)

            for x in range(min_x, max_x+1):
                board[x][y] = board[x][y] + 1
        elif line.orientation == Orientation.VERTICAL:
            x = line.start.x
            min_y = min(line.start.y, line.end.y)
            max_y = max(line.start.y, line.end.y)

            for y in range(min_y, max_y+1):
                board[x][y] = board[x][y] + 1
        else:
            min_y = min(line.start.y, line.end.y)
            max_y = max(line.start.y, line.end.y)
            min_x = min(line.start.x, line.end.x)
            max_x = max(line.start.x, line.end.x)

            upward = (line.start.y < line.end.y and line.start.x < line.end.x) or \
                     (line.start.y > line.end.y and line.start.x > line.end.x)

            for delta in range(max_x - min_x + 1):
                if upward:
                    board[min_x + delta][min_y + delta] = board[min_x + delta][min_y + delta] + 1
                else:
                    board[min_x + delta][max_y - delta] = board[min_x + delta][max_y - delta] + 1

    return board

if __name__ == '__main__':
    run()
