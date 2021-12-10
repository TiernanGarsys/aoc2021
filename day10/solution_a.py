# Advent of Code 2021, Day 10, Solution A

import sys

from collections import defaultdict
from functools import reduce

open_chars = { '(', '[', '{', '<' }

open_to_complement = {
    '(': ')', 
    '[': ']', 
    '{': '}', 
    '<': '>',
}

close_to_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file days')

    filename = sys.argv[1]
   
    lines = [] 
    with open(filename) as file:
        lines = [l.strip() for l in file.readlines()]

    errors = defaultdict(int)
    for line in lines:
        stack = []

        for c in line:
            if c in open_chars:
                stack.append(c)
            else:
                open_char = stack.pop() if stack else None

                if not open_char or c != open_to_complement[open_char]:
                    errors[c] += 1

    score = reduce(lambda a, i: a + (i[1] * close_to_score[i[0]]), errors.items(), 0)
    print('The answer is %i' % score)


if __name__ == '__main__':
    run()
