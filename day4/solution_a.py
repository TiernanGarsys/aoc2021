# Advent of Code 2021, Day 4, Solution A

import sys

from collections import defaultdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class Board():
    solutions: list[str]
    numbers: list[str]


def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file')

    filename = sys.argv[1]
   
    lines = []
    with open(filename) as file:
        lines = [r.strip() for r in file.readlines()]

    draws = list(map(int, lines[0].split(',')))
    boards = parse_boards(lines[1:])

    solved_board = None
    solution = None

    for idx in range(len(draws)):
        draws_to_consider = draws[:idx]
        solved_boards = list(filter(lambda b: check_board(b, draws_to_consider), boards))

        if len(solved_boards) > 0:
            solved_board = solved_boards[0]
            solution = draws_to_consider
            break
    
    score = get_score(solved_board, solution)
    print('The answer is %i' % score)

def parse_boards(lines):
    line_groups = []
    current_group = []
    line_groups.append(current_group)

    for line in lines:
        sanitized = line.strip()

        if not len(sanitized):
            # If we encounter an empty line, we've finished the prior group
            current_group = []
            line_groups.append(current_group)
        else: 
            current_group.append(list(map(int, line.split())))
   
    boards = []
    for group in line_groups:
        numbers = [n for line in group for n in line]
        solutions = []

        # Each parsed line is a horizontal solution.
        solutions.extend(group)

        for idx in range(len(group)):
            # Collect vertical solutions
            solutions.append(list(map(lambda x: x[idx], group)))

        boards.append(Board(solutions=solutions, numbers=numbers))

    return boards

def check_board(board, drawn_numbers):
    for solution in board.solutions:
        if all(num in drawn_numbers for num in solution):
            return True
    return False


def get_score(board, drawn_numbers):
    unmarked_sum = sum([n for n in board.numbers if n not in drawn_numbers])
    return unmarked_sum * drawn_numbers[-1]

if __name__ == '__main__':
    run()
