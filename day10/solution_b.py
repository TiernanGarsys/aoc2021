# Advent of Code 2021, Day 10, Solution B

import math
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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file days')

    filename = sys.argv[1]
   
    lines = [] 
    with open(filename) as file:
        lines = [l.strip() for l in file.readlines()]

    completions = []
    for line in lines:
        stack = []

        for c in line:
            valid = True
            if c in open_chars:
                stack.append(c)
            else:
                open_char = stack.pop() if stack else None

                if not open_char or c != open_to_complement[open_char]:
                    valid = False
                    break

        if valid:
            # Map the remaining unpaired brackets to their complements, and reverse the string.
            completions.append(reduce(lambda a, c: open_to_complement[c] + a, stack, ''))
            

    scores = [reduce(lambda a, i: 5 * a + close_to_score[i[0]], c, 0) for c in completions]
    median = sorted(scores)[math.floor(len(scores)/2)]
    print('The answer is %i' % median)


if __name__ == '__main__':
    run()
