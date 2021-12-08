# Advent of Code 2023, Day 8, Solution A

import sys

from collections import defaultdict


def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file days')

    filename = sys.argv[1]

    signals = []
    displays = []
    with open(filename) as file:
        for line in file.readlines():
            sections = line.split('|')
            signals.append(sections[0].split())
            displays.append(sections[1].split())

    length_to_freq = defaultdict(int)
    for display in displays:
        for digit in display:
            length_to_freq[len(digit)] += 1
    
    answer = length_to_freq[2] + length_to_freq[3] + length_to_freq[4] + length_to_freq[7] 
    print('The answer is %i' % answer)

if __name__ == '__main__':
    run()
