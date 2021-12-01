# Advent of Code 2021, Day 1

import sys

def run():
    if len(sys.argv) < 3:
        raise ValueError('No arguments provided. Usage: solution.py input_file window_size')

    filename = sys.argv[1]
    window_size = int(sys.argv[2])

    depths = []

    with open(filename) as file:
        depths = [int(depth) for depth in file.readlines()]

    segments = []
    for idx in range(0, len(depths) - window_size):
        segments.append(sum(depths[idx:idx+window_size+1]))

    increases = sum(segments[idx] > segments[idx-1] for idx in range(1, len(segments)))

    print('Depth data contains %s increases' % increases)

if __name__ == '__main__':
    run()
