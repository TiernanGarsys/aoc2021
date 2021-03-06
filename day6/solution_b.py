# Advent of Code 2021, Day 6, Solution B

import sys

from dataclasses import dataclass

def run():
    if len(sys.argv) < 3:
        raise ValueError('No arguments provided. Usage: solution.py input_file days')

    filename = sys.argv[1]
    days_to_simulate = int(sys.argv[2])
   
    initial_fishies = []
    with open(filename) as file:
        initial_fishies = [int(f) for f in file.read().split(',')]

    fish_ring = [0] * 9
    for f in initial_fishies:
        fish_ring[f] += 1

    for d in range(days_to_simulate):
        fish_to_spawn = fish_ring[0]
        fish_ring = fish_ring[1:] + [fish_ring[0]]
        fish_ring[6] = fish_ring[6] + fish_to_spawn

    print('The answer is %i' % sum(fish_ring))

if __name__ == '__main__':
    run()
